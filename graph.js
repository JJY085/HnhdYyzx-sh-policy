const graphData=document.querySelector('#graph-data');
if(graphData){
 const {policies,relations}=JSON.parse(graphData.textContent);
 const select=document.querySelector('#graph-select'),focus=document.querySelector('#graph-focus');
 const nodes=document.querySelector('#graph-nodes'),lines=document.querySelector('#graph-lines'),canvas=document.querySelector('#graph-canvas'),space=document.querySelector('#graph-space');
 let selected='',zoom=1;
 const levels=['国家','长三角','上海'],labels=['国家基础','区域协同','上海细则'];
 function draw(){
  const linked=relations.filter(r=>r.source===selected||r.target===selected);
  const neighbors=new Set([selected,...linked.flatMap(r=>[r.source,r.target])]);
  const visible=policies.filter(p=>!selected||!focus.checked||neighbors.has(p.id));
  const positions=new Map();const counts=levels.map(l=>visible.filter(p=>p.level===l).length);
  const height=Math.max(340,80+Math.max(...counts)*110),width=1080;
  canvas.style.width=width+'px';canvas.style.height=height+'px';canvas.style.transform=`scale(${zoom})`;
  space.style.width=width*zoom+'px';space.style.height=height*zoom+'px';
  nodes.replaceChildren();lines.replaceChildren();lines.setAttribute('viewBox',`0 0 ${width} ${height}`);lines.setAttribute('width',width);lines.setAttribute('height',height);
  const ns='http://www.w3.org/2000/svg';const defs=document.createElementNS(ns,'defs'),marker=document.createElementNS(ns,'marker');marker.id='graph-arrow';marker.setAttribute('viewBox','0 0 10 10');marker.setAttribute('refX','9');marker.setAttribute('refY','5');marker.setAttribute('markerWidth','6');marker.setAttribute('markerHeight','6');marker.setAttribute('orient','auto-start-reverse');const arrow=document.createElementNS(ns,'path');arrow.setAttribute('d','M 0 0 L 10 5 L 0 10 z');arrow.setAttribute('fill','#034a92');marker.append(arrow);defs.append(marker);lines.append(defs);
  levels.forEach((level,col)=>{
   const heading=document.createElement('div');heading.className='graph-column';heading.textContent=labels[col];heading.style.left=(35+col*355)+'px';nodes.append(heading);
   visible.filter(p=>p.level===level).forEach((p,row)=>{
    const x=35+col*355,y=65+row*110;positions.set(p.id,{x,y});
    const button=document.createElement('button');button.type='button';button.className='graph-node '+['national','regional','shanghai'][col];button.style.left=x+'px';button.style.top=y+'px';button.dataset.graphSelect=p.id;button.setAttribute('aria-pressed',String(p.id===selected));
    if(selected&&!neighbors.has(p.id))button.classList.add('graph-dim');
    const title=document.createElement('strong');title.textContent=p.title;const status=document.createElement('small');status.textContent=p.status;button.append(title,status);button.addEventListener('click',()=>choose(p.id));nodes.append(button);
   });
  });
  const edges=relations.filter(r=>positions.has(r.source)&&positions.has(r.target));
  edges.forEach(r=>{
   const a=positions.get(r.source),b=positions.get(r.target);let d;
   if(a.x===b.x){const x=a.x+280,ay=a.y+42,by=b.y+42;d=`M${x},${ay} C${x+42},${ay} ${x+42},${by} ${x},${by}`;}
   else{const forward=a.x<b.x,ax=a.x+(forward?280:0),bx=b.x+(forward?0:280),mid=(ax+bx)/2;d=`M${ax},${a.y+42} C${mid},${a.y+42} ${mid},${b.y+42} ${bx},${b.y+42}`;}
   const path=document.createElementNS(ns,'path');path.setAttribute('d',d);path.setAttribute('class','graph-edge'+(r.type==='related'?' related':'')+(selected&&(r.source===selected||r.target===selected)?' emphasized':''));if(r.type!=='related')path.setAttribute('marker-end','url(#graph-arrow)');lines.append(path);
  });
  document.querySelector('#graph-scale').textContent=Math.round(zoom*100)+'%';
  document.querySelector('#graph-message').textContent=`${visible.length} 个政策节点 · ${edges.length} 条关系${selected?' · 已选中：'+policies.find(p=>p.id===selected).title:''}`;
 }
 function choose(id){selected=id;select.value=id;document.querySelectorAll('.graph-detail').forEach(el=>el.hidden=el.id!=='inspect-'+id);document.querySelector('#graph-welcome').hidden=!!id;draw();}
 select.addEventListener('change',()=>choose(select.value));focus.addEventListener('change',draw);
 document.querySelector('#graph-reset').addEventListener('click',()=>{zoom=1;choose('');});
 document.querySelector('#graph-plus').addEventListener('click',()=>{zoom=Math.min(1.4,Math.round((zoom+.1)*10)/10);draw();});
 document.querySelector('#graph-minus').addEventListener('click',()=>{zoom=Math.max(.6,Math.round((zoom-.1)*10)/10);draw();});
 document.querySelectorAll('.graph-inspector [data-graph-select]').forEach(el=>el.addEventListener('click',()=>choose(el.dataset.graphSelect)));
 draw();
}
