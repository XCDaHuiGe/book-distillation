import json
import re
from pathlib import Path

def parse_logic_seed(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    nodes = []
    edges = []
    node_ids = set()

    def add_node(nid, label, ntype, source_file, chapter_range=None):
        if nid not in node_ids:
            nodes.append({
                'id': nid, 'label': label, 'type': ntype,
                'source_file': source_file, 'chapter_range': chapter_range or ''
            })
            node_ids.add(nid)

    def add_edge(src, tgt, relation, confidence='INFERRED', weight=0.8):
        if src in node_ids and tgt in node_ids:
            edges.append({
                'source': src, 'target': tgt, 'relation': relation,
                'confidence': confidence, 'weight': weight
            })

    # === 人物节点 ===
    characters = {
        'chr_xiaoyan': ('萧炎', '主角'),
        'chr_yaochen': ('药老/药尘', '导师/药族'),
        'chr_xuner': ('薰儿/古薰儿', '女主/古族'),
        'chr_cailin': ('彩鳞/美杜莎', '蛇人族女王'),
        'chr_yixian': ('小医仙', '厄难毒体'),
        'chr_ziyan': ('紫研', '太虚古龙'),
        'chr_yunyun': ('云韵/云芝', '云岚宗宗主'),
        'chr_nalan': ('纳兰嫣然', '退婚者'),
        'chr_yunshan': ('云山', '云岚宗老宗主/魂殿合作者'),
        'chr_haibodong': ('海波东', '冰皇'),
        'chr_hanfeng': ('韩枫', '药老叛徒'),
        'chr_huntian': ('魂天帝', '最终BOSS'),
        'chr_hundian': ('魂殿殿主', '魂殿首领'),
        'chr_xiaochen': ('萧晨', '萧族先祖'),
        'chr_xiaoxuan': ('萧玄', '萧族族长'),
        'chr_guque': ('古元', '古族族长'),
        'chr_yaodan': ('药丹', '药族族长'),
        'chr_tangzhen': ('唐震', '焚炎谷主'),
        'chr_fengzun': ('风尊者', '星陨阁'),
        'chr_tianhuo': ('天火尊者', '曜天火'),
        'chr_hunxu': ('魂虚子', '魂族丹会'),
        'chr_beilong': ('北龙王', '太虚古龙叛王'),
        'chr_zhuyan': ('烛离', '东龙岛大长老'),
    }

    for nid, (label, desc) in characters.items():
        add_node(nid, f'{label}({desc})', 'CHR', 'logic_seed.md')

    # === 异火节点 ===
    fires = {
        'fire_qlxh': ('青莲地心火', '#19', 'Ch90-98'),
        'fire_ylxy': ('陨落心炎', '#14', 'Ch255-268'),
        'fire_hxy': ('海心焰', '#15', 'Ch448'),
        'fire_glh': ('骨灵冷火', '#11', 'Ch640-648'),
        'fire_jllg': ('九龙雷罡火', '#12', 'Ch888-900'),
        'fire_sqyy': ('三千焱炎火', '#9', 'Ch1094-1100'),
        'fire_jlyh': ('净莲妖火', '#3', 'Ch1311-1345'),
        'fire_xwty': ('虚无吞炎', '#2', '后期'),
        'fire_tushe': ('陀舍古帝火', '#1', '最终'),
    }

    for nid, (name, rank, chapter) in fires.items():
        add_node(nid, f'{name}(#{rank})', 'FIRE', 'logic_seed.md', chapter)

    # === 势力节点 ===
    factions = {
        'fct_yunlan': ('云岚宗', '加玛帝国第一宗门'),
        'fct_jianan': ('迦南学院', '斗气大陆最高学府'),
        'fct_hundian': ('魂殿', '魂族爪牙/最大反派组织'),
        'fct_danta': ('丹塔', '炼药师圣地'),
        'fct_guzu': ('古族', '远古八族之一'),
        'fct_hunzu': ('魂族', '远古八族/最终反派'),
        'fct_yaozu': ('药族', '远古八族/炼药世家'),
        'fct_yanmeng': ('炎盟', '萧炎创立的加玛帝国联盟'),
        'fct_tianfu': ('天府联盟', '中州抗魂殿联盟'),
        'fct_fenyan': ('焚炎谷', '中州三谷之一'),
        'fct_taixu': ('太虚古龙族', '魔兽界最强种族'),
        'fct_xingyun': ('星陨阁', '药老创建/风尊者守护'),
        'fct_huazong': ('花宗', '中州二宗之一'),
        'fct_tianming': ('天冥宗', '中州二宗之一'),
    }

    for nid, (name, desc) in factions.items():
        add_node(nid, f'{name}({desc})', 'FCT', 'logic_seed.md')

    # === 空间节点 ===
    spaces = {
        'spc_moshan': ('魔兽山脉', '试炼起点'),
        'spc_sheren': ('蛇人族圣城', '美杜莎领地'),
        'spc_heijiao': ('黑角域', '混乱之地'),
        'spc_zhongzhou': ('中州', '大陆中心'),
        'spc_danyu': ('丹域', '炼药师圣地'),
        'spc_xingyu': ('星域', '三千焱炎火封印地'),
        'spc_tianmu': ('天墓', '古族试炼空间'),
        'spc_yaohuo': ('净莲妖火空间', '最终副本'),
        'spc_gudi': ('古帝洞府', '陀舍古帝传承'),
        'spc_jiuyou': ('九幽黄泉', '彩鳞传承地'),
    }

    for nid, (name, desc) in spaces.items():
        add_node(nid, f'{name}({desc})', 'SPC', 'logic_seed.md')

    # === 事件节点 ===
    events = {
        'evt_tuihun': ('退婚事件', 'Ch1', '故事起点'),
        'evt_sannian': ('三年之约决战', 'Ch339', '第一幕高潮'),
        'evt_yunlan': ('云岚宗大战', 'Ch249', '第一幕终章'),
        'evt_yunluo': ('陨落心炎爆发', 'Ch520', '内院危机'),
        'evt_hanfeng': ('韩枫之战', 'Ch590', '同门生死战'),
        'evt_danhui': ('丹会冠军', 'Ch1050', '炼药巅峰'),
        'evt_yaohuo': ('净莲妖火降世', 'Ch1310', '后期关键'),
        'evt_hundian': ('魂殿决战', 'Ch1450', '天府VS魂殿'),
        'evt_zhongji': ('最终之战', 'Ch1641', '封印魂天帝'),
        'evt_doudi': ('突破斗帝', 'Ch1648', '炎帝诞生'),
    }

    for nid, (name, chapter, desc) in events.items():
        add_node(nid, f'{name}({desc})', 'EVT', 'logic_seed.md', chapter)

    # === 功法/技术节点 ===
    techniques = {
        'tec_fenjue': ('焚决', '核心功法/吞噬异火进化'),
        'tec_tianhuo': ('天火三玄变', '三重增幅秘法'),
        'tec_fonu': ('佛怒火莲', '异火融合斗技'),
        'tec_huiquan': ('毁灭火莲', '终极火莲变体'),
        'tec_huangquan': ('黄泉天怒', '灵魂音波斗技'),
    }

    for nid, (name, desc) in techniques.items():
        add_node(nid, f'{name}({desc})', 'TEC', 'logic_seed.md')

    # === 物品节点 ===
    items = {
        'itm_yaojie': ('纳戒', '药老栖身空间'),
        'itm_poyuan': ('破厄丹', '六品丹药/美杜莎交易'),
        'itm_youhai': ('幽海纳戒', '韩枫遗物'),
        'itm_puti': ('菩提大还丹', '九品宝丹'),
        'itm_yinyang': ('阴阳命魂丹', '药老躯体材料'),
    }

    for nid, (name, desc) in items.items():
        add_node(nid, f'{name}({desc})', 'ITM', 'logic_seed.md')

    # === 关系边 ===

    # 人物关系
    add_edge('chr_xiaoyan', 'chr_yaochen', '师徒', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'chr_xuner', '恋人', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'chr_cailin', '伴侣/战友', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'chr_yixian', '战友/暗恋', 'EXTRACTED', 0.9)
    add_edge('chr_xiaoyan', 'chr_ziyan', '义兄妹', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'chr_yunyun', '暧昧/对手', 'EXTRACTED', 0.9)
    add_edge('chr_xiaoyan', 'chr_nalan', '退婚/和解', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'chr_hanfeng', '弑师仇人', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'chr_huntian', '最终对手', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'chr_xiaochen', '先祖/战友', 'EXTRACTED', 0.9)
    add_edge('chr_xiaoyan', 'chr_xiaoxuan', '先祖传承', 'EXTRACTED', 0.8)
    add_edge('chr_yaochen', 'chr_hanfeng', '弑师', 'EXTRACTED', 1.0)
    add_edge('chr_yaochen', 'chr_fengzun', '挚友', 'EXTRACTED', 1.0)
    add_edge('chr_cailin', 'chr_xuner', '竞争/共存', 'INFERRED', 0.7)
    add_edge('chr_yunshan', 'chr_hundian', '合作', 'EXTRACTED', 0.9)
    add_edge('chr_huntian', 'chr_hundian', '上级→下级', 'EXTRACTED', 1.0)

    # 人物→势力
    add_edge('chr_xiaoyan', 'fct_yanmeng', '创立', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'fct_tianfu', '创立', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'fct_jianan', '学员', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'fct_xingyun', '继承', 'EXTRACTED', 0.9)
    add_edge('chr_yaochen', 'fct_xingyun', '创立', 'EXTRACTED', 1.0)
    add_edge('chr_yaochen', 'fct_danta', '八品炼药师', 'EXTRACTED', 1.0)
    add_edge('chr_yaochen', 'fct_yaozu', '出身', 'EXTRACTED', 1.0)
    add_edge('chr_xuner', 'fct_guzu', '神品血脉', 'EXTRACTED', 1.0)
    add_edge('chr_ziyan', 'fct_taixu', '龙皇血脉', 'EXTRACTED', 1.0)
    add_edge('chr_tangzhen', 'fct_fenyan', '谷主', 'EXTRACTED', 1.0)
    add_edge('chr_yunshan', 'fct_yunlan', '老宗主', 'EXTRACTED', 1.0)
    add_edge('chr_yunyun', 'fct_yunlan', '宗主', 'EXTRACTED', 1.0)

    # 人物→异火
    add_edge('chr_xiaoyan', 'fire_qlxh', '吞噬', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'fire_ylxy', '吞噬', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'fire_hxy', '回收', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'fire_glh', '继承', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'fire_jllg', '获得', 'EXTRACTED', 0.9)
    add_edge('chr_xiaoyan', 'fire_sqyy', '降服', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'fire_jlyh', '炼化', 'EXTRACTED', 1.0)
    add_edge('chr_hanfeng', 'fire_hxy', '持有', 'EXTRACTED', 1.0)

    # 异火→异火 (融合/吞噬)
    add_edge('fire_qlxh', 'fire_ylxy', '佛怒火莲融合', 'EXTRACTED', 1.0)
    add_edge('fire_jlyh', 'fire_xwty', '净莲妖圣对战', 'EXTRACTED', 0.8)

    # 人物→功法
    add_edge('chr_xiaoyan', 'tec_fenjue', '修炼', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'tec_tianhuo', '修炼', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'tec_fonu', '创造/使用', 'EXTRACTED', 1.0)
    add_edge('chr_xiaoyan', 'tec_huiquan', '创造/使用', 'EXTRACTED', 0.9)
    add_edge('chr_yaochen', 'tec_fenjue', '传授', 'EXTRACTED', 0.9)
    add_edge('tec_fenjue', 'fire_qlxh', '吞噬后进化', 'EXTRACTED', 1.0)

    # 功法→异火
    add_edge('tec_fonu', 'fire_qlxh', '使用', 'EXTRACTED', 1.0)
    add_edge('tec_fonu', 'fire_ylxy', '使用', 'EXTRACTED', 1.0)

    # 事件→人物
    add_edge('evt_tuihun', 'chr_xiaoyan', '触发者', 'EXTRACTED', 1.0)
    add_edge('evt_tuihun', 'chr_nalan', '执行者', 'EXTRACTED', 1.0)
    add_edge('evt_sannian', 'chr_xiaoyan', '执行者', 'EXTRACTED', 1.0)
    add_edge('evt_sannian', 'chr_nalan', '对手', 'EXTRACTED', 1.0)
    add_edge('evt_yunlan', 'chr_xiaoyan', '执行者', 'EXTRACTED', 1.0)
    add_edge('evt_yunlan', 'chr_yunshan', '对手', 'EXTRACTED', 1.0)
    add_edge('evt_yunluo', 'chr_xiaoyan', '受益者', 'EXTRACTED', 1.0)
    add_edge('evt_yunluo', 'fire_ylxy', '爆发', 'EXTRACTED', 1.0)
    add_edge('evt_hanfeng', 'chr_xiaoyan', '复仇者', 'EXTRACTED', 1.0)
    add_edge('evt_hanfeng', 'chr_hanfeng', '被杀', 'EXTRACTED', 1.0)
    add_edge('evt_danhui', 'chr_xiaoyan', '冠军', 'EXTRACTED', 1.0)
    add_edge('evt_danhui', 'fct_danta', '主办', 'EXTRACTED', 1.0)
    add_edge('evt_yaohuo', 'chr_xiaoyan', '炼化者', 'EXTRACTED', 1.0)
    add_edge('evt_yaohuo', 'fire_jlyh', '核心', 'EXTRACTED', 1.0)
    add_edge('evt_hundian', 'chr_xiaoyan', '统帅', 'EXTRACTED', 1.0)
    add_edge('evt_hundian', 'fct_tianfu', '参战', 'EXTRACTED', 1.0)
    add_edge('evt_hundian', 'fct_hundian', '被剿灭', 'EXTRACTED', 1.0)
    add_edge('evt_zhongji', 'chr_xiaoyan', '主角', 'EXTRACTED', 1.0)
    add_edge('evt_zhongji', 'chr_huntian', '对手', 'EXTRACTED', 1.0)
    add_edge('evt_doudi', 'chr_xiaoyan', '突破者', 'EXTRACTED', 1.0)

    # 事件→空间
    add_edge('evt_sannian', 'fct_yunlan', '发生在', 'EXTRACTED', 1.0)
    add_edge('evt_danhui', 'spc_danyu', '发生在', 'EXTRACTED', 1.0)
    add_edge('evt_yaohuo', 'spc_yaohuo', '发生在', 'EXTRACTED', 1.0)
    add_edge('evt_zhongji', 'spc_gudi', '发生在', 'EXTRACTED', 1.0)

    # 势力关系
    add_edge('fct_yanmeng', 'fct_yunlan', '取代', 'EXTRACTED', 0.9)
    add_edge('fct_tianfu', 'fct_hundian', '对抗', 'EXTRACTED', 1.0)
    add_edge('fct_guzu', 'fct_hunzu', '敌对', 'EXTRACTED', 1.0)
    add_edge('fct_hunzu', 'fct_yaozu', '毁灭', 'EXTRACTED', 1.0)
    add_edge('fct_hundian', 'fct_hunzu', '隶属', 'EXTRACTED', 1.0)

    # 空间层级
    add_edge('spc_moshan', 'spc_zhongzhou', '通往', 'INFERRED', 0.6)
    add_edge('spc_zhongzhou', 'spc_danyu', '包含', 'EXTRACTED', 1.0)
    add_edge('spc_zhongzhou', 'spc_yaohuo', '副本入口', 'EXTRACTED', 0.9)
    add_edge('spc_zhongzhou', 'spc_gudi', '副本入口', 'EXTRACTED', 0.9)

    return {'nodes': nodes, 'edges': edges}


def build_visualization_html(graph_data, output_path):
    nodes = graph_data['nodes']
    edges = graph_data['edges']

    categories = {'CHR': '人物', 'FIRE': '异火', 'FCT': '势力',
                  'SPC': '空间', 'EVT': '事件', 'TEC': '功法', 'ITM': '物品'}
    colors = {'CHR': '#e06060', 'FIRE': '#ff8040', 'FCT': '#4080e0',
              'SPC': '#40a060', 'EVT': '#c080e0', 'TEC': '#e0c040', 'ITM': '#40c0c0'}

    node_map = {n['id']: n for n in nodes}
    edge_list = []
    for e in edges:
        edge_list.append({
            'source': e['source'], 'target': e['target'],
            'relation': e['relation'], 'confidence': e['confidence']
        })

    chart_data = json.dumps({'nodes': nodes, 'edges': edge_list, 'categories': categories, 'colors': colors})

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>斗破苍穹 知识图谱</title>
<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a0a14;color:#c8c8d4;font-family:"Microsoft YaHei",sans-serif;overflow:hidden;height:100vh}}
#graph{{width:100vw;height:100vh}}
.tooltip{{position:fixed;background:rgba(20,20,40,0.95);border:1px solid rgba(212,165,116,0.4);border-radius:8px;
  padding:12px 16px;font-size:14px;pointer-events:none;z-index:9999;display:none;max-width:320px}}
.tooltip .name{{color:#f0d6a8;font-size:16px;font-weight:bold;margin-bottom:4px}}
.tooltip .type{{color:#8888a0;font-size:12px}}
.legend{{position:fixed;bottom:20px;left:20px;display:flex;gap:12px;flex-wrap:wrap;z-index:100}}
.legend-item{{display:flex;align-items:center;gap:6px;font-size:13px;color:#8888a0;cursor:pointer;padding:4px 8px;
  border-radius:4px;transition:all .2s}}
.legend-item:hover{{background:rgba(255,255,255,0.05)}}
.legend-dot{{width:10px;height:10px;border-radius:50%}}
.title{{position:fixed;top:16px;left:20px;font-size:18px;color:#f0d6a8;z-index:100;font-weight:bold}}
.subtitle{{position:fixed;top:16px;left:calc(20px + 180px);font-size:13px;color:#8888a0;z-index:100;padding-top:3px}}
</style>
</head>
<body>
<div class="title">斗破苍穹 知识图谱</div>
<div class="subtitle">1648章 · 全量实体关系图 · V3.1</div>
<div id="graph"></div>
<div id="tooltip" class="tooltip"></div>
<div class="legend" id="legend"></div>

<script>
var chartData = {chart_data};

var chart = echarts.init(document.getElementById('graph'));

function buildGraph() {{
    var nodes = chartData.nodes.map(function(n) {{
        return {{
            id: n.id, name: n.label, category: Object.keys(chartData.categories).indexOf(n.type),
            symbolSize: n.type === 'CHR' ? 24 : (n.type === 'EVT' ? 28 : (n.type === 'FCT' ? 22 : 16)),
            itemStyle: {{ color: chartData.colors[n.type] }},
            label: {{ show: true, fontSize: 11, color: '#c8c8d4' }}
        }};
    }});

    var links = chartData.edges.map(function(e) {{
        return {{
            source: e.source, target: e.target,
            label: {{ show: true, formatter: e.relation, fontSize: 9, color: '#888' }},
            lineStyle: {{
                color: e.confidence === 'EXTRACTED' ? 'rgba(212,165,116,0.4)' : 'rgba(123,79,160,0.3)',
                width: e.confidence === 'EXTRACTED' ? 1.5 : 0.8,
                curveness: 0.2
            }}
        }};
    }});

    var categories = [];
    for (var k in chartData.categories) {{
        categories.push({{ name: chartData.categories[k], itemStyle: {{ color: chartData.colors[k] }} }});
    }}

    return {{ nodes: nodes, links: links, categories: categories }};
}}

var graph = buildGraph();

var option = {{
    tooltip: {{}},
    legend: [{{
        data: graph.categories.map(function(c){{return c.name}}),
        bottom: 20, left: 'center', textStyle: {{ color: '#8888a0', fontSize: 12 }}
    }}],
    series: [{{
        type: 'graph', layout: 'force', force: {{ repulsion: 300, edgeLength: [120, 280], gravity: 0.1 }},
        roam: true, draggable: true,
        data: graph.nodes, links: graph.links, categories: graph.categories,
        lineStyle: {{ opacity: 0.7, curveness: 0.2 }},
        emphasis: {{ focus: 'adjacency', lineStyle: {{ width: 3 }} }},
        label: {{ show: true, position: 'right', fontSize: 11, color: '#c8c8d4' }}
    }}]
}};

chart.setOption(option);

chart.on('click', function(params) {{
    if (params.dataType === 'node') {{
        var n = chartData.nodes.find(function(x){{return x.id === params.data.id}});
        if (n) {{
            var tooltip = document.getElementById('tooltip');
            tooltip.innerHTML = '<div class="name">' + n.label + '</div>' +
                '<div class="type">' + (chartData.categories[n.type]||n.type) + ' · ' + (n.chapter_range||'') + '</div>';
            tooltip.style.display = 'block';
            tooltip.style.left = (params.event.event.clientX + 12) + 'px';
            tooltip.style.top = (params.event.event.clientY - 40) + 'px';
        }}
    }}
}});

document.addEventListener('click', function(e) {{
    if (!e.target.closest('#graph')) document.getElementById('tooltip').style.display = 'none';
}});

window.addEventListener('resize', function(){{chart.resize()}});
</script>
</body>
</html>'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    base = Path(__file__).parent.parent
    logic_seed_path = base / 'distillation_output' / 'logic_seed.md'
    graph_json_path = base / 'graphify-out' / 'graph.json'
    graph_html_path = base / 'graphify-out' / 'graph.html'
    (base / 'graphify-out').mkdir(exist_ok=True)

    graph_data = parse_logic_seed(str(logic_seed_path))
    print(f'知识图谱构建完成: {len(graph_data["nodes"])} 节点, {len(graph_data["edges"])} 关系边')

    with open(graph_json_path, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)
    print(f'graph.json 已保存: {graph_json_path}')

    build_visualization_html(graph_data, str(graph_html_path))
    print(f'graph.html 已保存: {graph_html_path}')

    cat_counts = {}
    for n in graph_data['nodes']:
        cat_counts[n['type']] = cat_counts.get(n['type'], 0) + 1
    print(f'节点分布: {cat_counts}')