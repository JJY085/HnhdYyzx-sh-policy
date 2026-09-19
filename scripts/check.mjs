import fs from 'node:fs';import assert from 'node:assert/strict';
const p=JSON.parse(fs.readFileSync('src/data/policies.json'));const r=JSON.parse(fs.readFileSync('src/data/policy-relations.json'));const ids=new Set(p.map(x=>x.id));assert.equal(ids.size,p.length);assert.equal(p.length,29);for(const x of p){assert(x.title&&x.status);assert(fs.existsSync(`dist/policies/${x.id.toLowerCase()}/index.html`));for(const key of ['official_url','official_fulltext_url'])if(x[key]){const u=new URL(x[key]);assert.equal(u.protocol,'https:');assert(/(^|\.)(gov\.cn|sgcc\.com\.cn)$/.test(u.hostname));}for(const key of ['supersedes','superseded_by'])if(x[key])assert(ids.has(x[key]));}for(const x of r)assert(ids.has(x.source)&&ids.has(x.target));assert.equal(p.find(x=>x.id==='POLICY-EC005').status,'征求意见');assert.equal(p.find(x=>x.id==='POLICY-PENDING-001').status,'编制中');assert.equal(p.find(x=>x.id==='POLICY-SH001').status,'结算试运行');
const files=fs.readdirSync('dist',{recursive:true}).filter(x=>x.endsWith('.html'));for(const f of files){const html=fs.readFileSync('dist/'+f,'utf8');assert.equal((html.match(/<h1[ >]/g)||[]).length,1,f);assert(html.includes('name="description"'));assert(!html.includes('/Users/'));for(const m of html.matchAll(/(?:href|src)="(\/[^"?#]*)/g)){const base=(process.env.BASE_PATH||'').replace(/\/$/,'');assert(!base||m[1].startsWith(base+'/'));const path='dist'+m[1].slice(base.length);assert(fs.existsSync(path)||fs.existsSync(path+'/index.html'),`${f}: ${path}`);}}console.log(`Passed: ${files.length} pages, ${p.length} records, ${r.length} relationships, internal links and status invariants`);

const added=p.filter(x=>x.batch===2);assert.equal(added.length,8);for(const x of added){for(const k of ['background','main_content','core_rules','participant_relevance'])assert(x[k]?.length>20);if(!x.official_url){assert(x.missing_source_reason);assert.equal(x.status,'待补全文');const h=fs.readFileSync(`dist/policies/${x.id.toLowerCase()}/index.html`,'utf8');assert(h.includes('官方链接缺失原因'));assert(!h.includes('查看官方发布页'));}}assert.equal(p.filter(x=>x.title==='2026年上海市电力直接交易年度工作方案').length,1);

// A revision excerpt must not be presented as a complete, fully effective text.
const spot=p.find(x=>x.id==='POLICY-SH001');
assert.equal(spot.effective_date,null);
assert.equal(spot.official_fulltext_url,null);
assert(spot.official_url.endsWith('fileId=n06f7b76dccf54c259804bcba13073dfd'));
assert.equal(spot.version_history.find(v=>v.id==='2025-r1').changes.length,0);
const spotHtml=fs.readFileSync('dist/policies/policy-sh001/index.html','utf8');
assert(spotHtml.includes('2025年第二次修订重点衔接'));
assert(spotHtml.includes('暂不取消发电侧超额收益回收'));
assert(spotHtml.includes('沪发改能源〔2025〕206号'));
assert.equal((spotHtml.match(/class="version-entry"/g)||[]).length,3);
console.log('Passed: revision gaps, official source, date uncertainty and year rendering');
