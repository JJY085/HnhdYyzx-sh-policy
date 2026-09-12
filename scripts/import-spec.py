import re,json,pathlib
s=pathlib.Path('docs/project-spec.md').read_text()
ps=[]
for m in re.finditer(r'^## (POLICY-[A-Z0-9-]+)\n(.*?)(?=^## POLICY-|^# \d|\Z)',s,re.M|re.S):
 id,b=m.groups(); title=re.search(r'^### (.+)',b,re.M).group(1).strip('《》')
 p={k:None for k in ['short_title','sub_category','document_no','publish_date','effective_date','official_url','official_fulltext_url','significance','participant_relevance','last_verified','supersedes','superseded_by']}
 p.update(id=id,title=title)
 for k,v in re.findall(r'^- (\w+): (.+)$',b,re.M):p[k]=v.strip('`')
 p['keywords']=[x.strip() for x in p.get('keywords','').split(',')]
 p['sections']={h:t.strip().strip('-').strip() for h,t in re.findall(r'\*\*([^*\n]+)\*\*\n(.*?)(?=\n\*\*|\Z)',b,re.S)}
 p['background']=p['sections'].get('背景与意义','')
 p['main_content']=p['sections'].get('主要内容','')
 p['core_rules']=p['sections'].get('核心规则','') if id!='POLICY-SH001' else ''
 p['participant_relevance']=p['sections'].get('对上海市场参与者的关系','')
 p['notes']=''
 p['verification']='发布信息待核验'
 p['source_date']='2026-09-12'
 p['short_title']=title
 p['status_note']=p['status']
 p['status']={'现行规则体系，2026年初进一步修订':'待核验','现行有效，但需与2025版国家中长期规则协同理解':'现行有效','执行中':'现行有效','现行试行':'试行'}.get(p['status'],p['status'])
 p['subjects']=[t for t in ['燃煤','燃气','核电','风电','光伏','生物质','储能','虚拟电厂','售电公司','批发用户','零售用户','电网企业'] if t in b or (t=='虚拟电厂' and 'VPP' in b)]
 ps.append(p)
pathlib.Path('src/data/policies.json').write_text(json.dumps(ps,ensure_ascii=False,indent=2)+'\n')
rels=[]
b=s.split('# 12. 政策关系')[1].split('# 13.')[0]
a=None; typ=None
for l in b.splitlines():
 if re.match(r'^POLICY-',l):a=l.strip(':')
 elif 'children:' in l:typ='implements'
 elif 'related:' in l:typ='related'
 elif '- POLICY-' in l:rels.append({'source':a,'target':l.strip()[2:],'type':typ})
pathlib.Path('src/data/policy-relations.json').write_text(json.dumps(rels,ensure_ascii=False,indent=2)+'\n')
print(len(ps),'policies;',len(rels),'relationships')
