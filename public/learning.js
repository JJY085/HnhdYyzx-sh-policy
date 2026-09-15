const learningView=document.querySelector('#learning-view');
if(learningView){
  const params=new URLSearchParams(location.search);
  const filtered=['q','level','category','subject','status','year'].some(k=>params.get(k));
  const all=params.get('view')==='all'||filtered||(!params.has('view')&&document.body.dataset.active==='list');
  learningView.hidden=all;
  document.querySelector('#all-view').hidden=!all;
  document.querySelector(all?'#view-all':'#view-map').setAttribute('aria-current','true');
}
