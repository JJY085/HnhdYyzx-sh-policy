import json,pathlib
f=pathlib.Path('src/data/policies.json'); ps=json.loads(f.read_text()); d={p['id']:p for p in ps}
for p in ps:
 if p['id']!='POLICY-SH001':p.update(verification='发布信息已核验；摘要以项目资料为基础',last_verified='2026-09-12')
def patch(id,**kw):d['POLICY-'+id].update(kw)
patch('N001',document_date='2024-04-25',official_fulltext_url='https://www.ndrc.gov.cn/xxgk/zcfb/fzggwl/202405/P020240510390953264943.pdf')
patch('N002',official_fulltext_url='https://www.ndrc.gov.cn/xxgk/zcfb/ghxwj/202512/P020251226622166557290.pdf')
for n,date in [('N003','2023-09-07'),('N005','2024-09-13'),('N006','2024-01-31')]:patch(n,document_date=date,notes='官方信息公开页所列日期为制发日期；发布日期暂沿用项目资料，尚未单独确认公开时间。')
patch('N005',core_rules='拟参与交易的经营主体应先办理市场注册，不能以未经核准的附加条件限制入市。\n注册信息共享，不要求同一主体重复注册；具有多重主体身份的，应按类别分别注册。\n注册信息变化后应在5个工作日内申请变更。',participant_relevance='上海售电公司、发电企业、电力用户和新型经营主体应据此核对注册材料、主体类别及变更义务。',notes='官方正文规定自发布之日起施行，有效期五年。信息公开页所列2024-09-13为制发日期。')
patch('N008',official_url='https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=20482',document_date='2025-01-27',publish_date='2025-02-09',core_rules='风电、太阳能发电上网电量原则上进入市场，项目可自行报价或接受市场价格。\n机制电价通过市场外差价结算发挥作用，不是交易报价。\n存量与增量项目以2025年6月1日投产时间为分界，执行安排由地方细化。',participant_relevance='上海新能源项目需结合本地实施通知，区分市场交易收益与机制差价结算。',notes='发布日期依据国家发展改革委通知目录；成文日期依据官方全文。生物质、地热项目由地方参照研究方案，不直接等同风光项目适用范围。')
patch('SH001',notes='官方文件为交易平台动态预览入口，本次未能读取正文并确认修订版、文号和日期。保留学习资料摘要，具体交易参数请查阅已确认版本的官方文件。',verification='动态预览正文及具体版本待核验')
patch('SH002',official_fulltext_url='https://hdj.nea.gov.cn/xxgk/fdzdgknr/gfxwj/hdnyjgfxwj/202603/P020260331593974942947.pdf',notes='已核对华东能源监管局规范性文件目录与附件链接。附件较大，本次未完成全文核验；文号和实施日期不作推断。',verification='官方目录与附件链接已核验；正文待核验')
patch('SH003',document_date='2026-02-10',effective_date='2026-04-01',notes='二级限价不是固定数值。日前或实时出清日均价超过二级限价上限时，对相应市场当日各时段出清价格按比例下调。具体数值以指定平台披露为准。')
patch('SH004',document_date='2025-07-30',status='试行',notes='官方正文明确本通知试行至2026年底。发布日期为2025-08-05，成文日期为2025-07-30，二者分别记录。')
patch('SH005',core_rules='绿色电力价格应区分电能量价格与绿证价格。\n零售用户原则上通过绑定的售电企业参与，售电企业需按规定完成零售侧合约分配。',participant_relevance='具有绿色消费需求的批发用户、零售用户与售电企业应关注合约分配、绿证及溯源责任。',notes='2024年地方方案需结合2025年国家中长期规则及新能源价格改革协同理解；具体适用以更新的正式政策为准。')
patch('SH006',document_date='2025-12-03',core_rules='本次竞价机制电价为0.4155元/千瓦时（含税），仅适用于对应入选项目。\n已投产入选项目自2026年1月1日结算，未投产项目原则上从申报投产之日的次月1日开始。',background='本通知落实新能源增量项目机制电价竞价，公布入选结果并明确结算衔接。',participant_relevance='入选项目应核对官方附件中的机制电量和执行期限，不能将竞价结果视作全部新能源项目的统一电价。')
patch('SH007',document_no='沪发改能源〔2026〕140号',issuer='上海市发展和改革委员会',document_date='2026-07-17',core_rules='项目区分单用户、多用户及并网型、离网型模式，明确主责单位和产权责任边界。\n并网型项目原则上作为整体参与市场，并按与公共电网交换功率结算。\n绿电直连上网电量不纳入可持续发展价格结算机制，也不参与机制电价竞价。',participant_relevance='绿电需求企业、园区和新能源投资方需共同核对项目主责、协议、计量与市场参与安排。')
patch('EC001',official_fulltext_url='https://hdj.nea.gov.cn/xxgk/fdzdgknr/gfxwj/hdnyjgfxwj/202604/P020260417606107102994.pdf',core_rules='适用于上海、江苏、浙江、安徽和福建已注册经营主体之间的跨省中长期交易。\n本细则不涉及零售市场，交易可覆盖数年、年度、月度和月内。',participant_relevance='上海购电主体研究市外电源与合同安排时，应同时考虑跨省规则和上海市内规则。',verification='官方目录、附件与适用范围已核验')
patch('EC002',core_rules='已启动市场交易的辅助服务品种执行对应市场规则，不按管理细则重复补偿。\n调度机构统计补偿与考核，交易机构出具结算依据，电网企业完成费用结算。',background='为华东区域系统安全与清洁能源消纳建立辅助服务调用、补偿和分摊制度。',participant_relevance='上海发电侧并网主体、储能和可调节负荷应核对适用调度范围、技术条件及补偿责任。')
patch('PENDING-001',notes='2026-09-08发布的是编制启动会报道，会议于9月3日召开；不是实施细则发布公告，不能据此填政策发布日期或实施日期。',core_rules='尚未正式发布，不构成可执行的交易规则。',main_content='官方报道披露编制启动工作，涉及市场衔接、费用分摊与职责分工讨论。',participant_relevance='相关企业可以跟踪编制及后续征求意见，不应按该条目制定已生效的交易参数。')
patch('EC005',notes='官方征求意见期为2026年8月28日至9月27日；截至本次核验仍应标为征求意见，不能作为正式交易依据。',core_rules='征求意见稿不等于正式生效规则，具体要求需等待正式文件确认。',background='为进一步规范长三角短期电力互济而征求社会意见。',main_content='官方公告公开征求短期电力互济交易实施细则意见，拟规范区域市场交易。',participant_relevance='上海相关经营主体可以关注征求意见内容与后续正式版本。')
for p in ps:p['verification_sources']=[u for u in [p.get('official_url'),p.get('official_fulltext_url')] if u]
f.write_text(json.dumps(ps,ensure_ascii=False,indent=2)+'\n')
