import json
from pathlib import Path

BASE = Path(__file__).parent

# Load existing cities
cities_text = (BASE / "data.js").read_text(encoding="utf-8")
# Extract existing cities array
cities_json_str = cities_text.replace("window.CITIES =", "").strip()
if cities_json_str.endswith(";"):
    cities_json_str = cities_json_str[:-1].strip()

# If data.js is already in new format, try loading prompts.json
try:
    cities_items = json.loads((BASE / "prompts.json").read_text(encoding="utf-8"))
    for c in cities_items:
        if "prompt" in c:
            del c["prompt"]
except Exception:
    cities_items = json.loads(cities_json_str)

zodiac_items = [
    {"id": 1, "name": "子鼠", "title": "鼠 · 灵鼠", "features": "机敏灵动的小鼠轮廓、捧着松果、灵巧胡须与尾巴线条", "keywords": ["灵动", "机敏", "丰裕"], "colors": "炭黑 · 砖红 · 赭石黄", "output": "images/zodiac/01_鼠.png"},
    {"id": 2, "name": "丑牛", "title": "牛 · 拓荒牛", "features": "沉稳雄浑的水牛轮廓、弯曲有力的双角、俯首耕耘与简练草甸线条", "keywords": ["沉稳", "耕耘", "坚韧"], "colors": "炭黑 · 砖红 · 深青灰", "output": "images/zodiac/02_牛.png"},
    {"id": 3, "name": "寅虎", "title": "虎 · 猛虎", "features": "威严矫健的卧虎轮廓、额间王字斑纹、苍劲山石与几笔松针", "keywords": ["威严", "王者", "山林"], "colors": "炭黑 · 朱砂红 · 赭黄", "output": "images/zodiac/03_虎.png"},
    {"id": 4, "name": "卯兔", "title": "兔 · 玉兔", "features": "灵巧温顺的玉兔轮廓、长耳直立、脚踏青草与桂花小枝", "keywords": ["温润", "灵巧", "月中"], "colors": "炭黑 · 砖红 · 柔灰", "output": "images/zodiac/04_兔.png"},
    {"id": 5, "name": "辰龙", "title": "龙 · 祥龙", "features": "盘旋升腾的祥龙轮廓、威严龙角、飘逸龙须与简练祥云水波线条", "keywords": ["祥瑞", "腾飞", "威仪"], "colors": "炭黑 · 朱红 · 赭金", "output": "images/zodiac/05_龙.png"},
    {"id": 6, "name": "巳蛇", "title": "蛇 · 灵蛇", "features": "灵动优雅的青蛇身姿、流线盘绕于几株修竹与灵芝草叶之间", "keywords": ["灵动", "修竹", "蜕变"], "colors": "炭黑 · 苔绿 · 朱红", "output": "images/zodiac/06_蛇.png"},
    {"id": 7, "name": "午马", "title": "马 · 骏马", "features": "昂首扬蹄的奔腾骏马轮廓、飘逸鬃毛、疾风与原野简线", "keywords": ["奔腾", "自由", "疾风"], "colors": "炭黑 · 赭石褐 · 砖红", "output": "images/zodiac/07_马.png"},
    {"id": 8, "name": "未羊", "title": "羊 · 瑞羊", "features": "瑞羊挺立的优雅轮廓、优美盘角、高山岩石与几簇青草", "keywords": ["和善", "吉祥", "登高"], "colors": "炭黑 · 砖红 · 草绿", "output": "images/zodiac/08_羊.png"},
    {"id": 9, "name": "申猴", "title": "猴 · 灵猴", "features": "机智灵动的猴子轮廓、双手捧桃、攀援老树藤蔓顾盼", "keywords": ["聪慧", "攀援", "福桃"], "colors": "炭黑 · 赭黄 · 朱红", "output": "images/zodiac/09_猴.png"},
    {"id": 10, "name": "酉鸡", "title": "鸡 · 雄鸡", "features": "引吭高歌的雄鸡轮廓、挺拔锯齿鸡冠、丰满翘起的尾羽", "keywords": ["破晓", "高昂", "守信"], "colors": "炭黑 · 朱砂红 · 赭黄", "output": "images/zodiac/10_鸡.png"},
    {"id": 11, "name": "戌狗", "title": "狗 · 灵犬", "features": "忠诚守望的灵犬轮廓、竖耳昂首、欢快卷尾与几穗麦芒", "keywords": ["忠诚", "守望", "温情"], "colors": "炭黑 · 赭黄 · 砖红", "output": "images/zodiac/11_狗.png"},
    {"id": 12, "name": "亥猪", "title": "猪 · 福猪", "features": "富足祥和的福猪轮廓、圆润健硕的身躯、谷仓与麦穗稻禾", "keywords": ["富足", "安详", "丰收"], "colors": "炭黑 · 砖红 · 土黄", "output": "images/zodiac/12_猪.png"},
]

solar_items = [
    {"id": 1, "name": "立春", "title": "立春 · 东风解冻", "features": "迎春花初绽、东风解冻与嫩绿柳芽吐露新枝", "keywords": ["东风", "初绿", "万物苏"], "season": "春", "colors": "炭黑 · 嫩绿 · 朱红", "output": "images/solar_terms/01_立春.png"},
    {"id": 2, "name": "雨水", "title": "雨水 · 獭祭鱼", "features": "细雨霏霏、春水初生微泛涟漪与初润草木", "keywords": ["润物", "微雨", "春水"], "season": "春", "colors": "炭黑 · 石板蓝 · 草绿", "output": "images/solar_terms/02_雨水.png"},
    {"id": 3, "name": "惊蛰", "title": "惊蛰 · 桃始华", "features": "春雷破土、初醒草木回春与萌动昆虫剪影", "keywords": ["春雷", "萌动", "蛰虫醒"], "season": "春", "colors": "炭黑 · 赭黄 · 石绿", "output": "images/solar_terms/03_惊蛰.png"},
    {"id": 4, "name": "春分", "title": "春分 · 玄鸟至", "features": "呢喃双燕归来剪影、桃花初绽与拂堤垂柳", "keywords": ["燕归", "桃红", "昼夜均"], "season": "春", "colors": "炭黑 · 桃粉红 · 柳绿", "output": "images/solar_terms/04_春分.png"},
    {"id": 5, "name": "清明", "title": "清明 · 桐始华", "features": "细雨霏霏、古朴瓦檐下几枝新柳与青团茶盏", "keywords": ["风清", "景明", "新柳"], "season": "春", "colors": "炭黑 · 艾绿 · 砖红", "output": "images/solar_terms/05_清明.png"},
    {"id": 6, "name": "谷雨", "title": "谷雨 · 萍始生", "features": "牡丹吐蕊盛放、甘雨润泽麦苗与水面浮萍", "keywords": ["雨生百谷", "牡丹", "暮春"], "season": "春", "colors": "炭黑 · 胭脂红 · 青绿", "output": "images/solar_terms/06_谷雨.png"},
    {"id": 7, "name": "立夏", "title": "立夏 · 蝼蝈鸣", "features": "初夏小荷才露尖尖角、蜻蜓伫立与槐树浓荫", "keywords": ["初荷", "立夏", "蝉未鸣"], "season": "夏", "colors": "炭黑 · 荷绿 · 朱红", "output": "images/solar_terms/07_立夏.png"},
    {"id": 8, "name": "小满", "title": "小满 · 苦菜秀", "features": "麦穗渐满灌浆饱满、芭蕉绿意与清泉潺潺", "keywords": ["麦粒满", "芭蕉", "未极盛"], "season": "夏", "colors": "炭黑 · 嫩麦黄 · 浓绿", "output": "images/solar_terms/08_小满.png"},
    {"id": 9, "name": "芒种", "title": "芒种 · 螳螂生", "features": "金黄成熟麦穗弯垂、水田插秧秧苗与螳螂剪影", "keywords": ["麦浪", "插秧", "收种"], "season": "夏", "colors": "炭黑 · 金黄 · 水蓝", "output": "images/solar_terms/09_芒种.png"},
    {"id": 10, "name": "夏至", "title": "夏至 · 鹿角解", "features": "高树鸣蝉、盛夏荷花怒放与盛阳日光波纹", "keywords": ["蝉鸣", "盛夏", "日最长"], "season": "夏", "colors": "炭黑 · 朱红 · 荷绿", "output": "images/solar_terms/10_夏至.png"},
    {"id": 11, "name": "小暑", "title": "小暑 · 温风至", "features": "晚风微热、荷塘水面流萤微光与蒲扇剪影", "keywords": ["温风", "流萤", "入伏"], "season": "夏", "colors": "炭黑 · 墨绿 · 荧光黄", "output": "images/solar_terms/11_小暑.png"},
    {"id": 12, "name": "大暑", "title": "大暑 · 腐草为萤", "features": "伏天浓翠绿荫、翠绿西瓜与骤雨云气", "keywords": ["大热", "浓荫", "雷雨"], "season": "夏", "colors": "炭黑 · 翠绿 · 朱红", "output": "images/solar_terms/12_大暑.png"},
    {"id": 13, "name": "立秋", "title": "立秋 · 凉风至", "features": "梧桐一叶飘落知秋、秋风微抚与初秋远山轮廓", "keywords": ["一叶落", "凉风", "新秋"], "season": "秋", "colors": "炭黑 · 赭黄 · 砖红", "output": "images/solar_terms/13_立秋.png"},
    {"id": 14, "name": "处暑", "title": "处暑 · 禾乃登", "features": "禾谷成熟金黄、秋高气爽天空与归雁一行", "keywords": ["出暑", "禾谷", "秋水清"], "season": "秋", "colors": "炭黑 · 金黄 · 秋褐", "output": "images/solar_terms/14_处暑.png"},
    {"id": 15, "name": "白露", "title": "白露 · 鸿雁来", "features": "清晨草尖凝结晶莹露珠、秋水芦苇与南飞鸿雁", "keywords": ["凝露", "芦花", "雁南飞"], "season": "秋", "colors": "炭黑 · 天蓝 · 草绿", "output": "images/solar_terms/15_白露.png"},
    {"id": 16, "name": "秋分", "title": "秋分 · 雷始收声", "features": "金桂飘香小花簇、丹枫叶片与秋分明月高挂", "keywords": ["金桂", "丹枫", "平分秋色"], "season": "秋", "colors": "炭黑 · 枫红 · 桂花黄", "output": "images/solar_terms/16_秋分.png"},
    {"id": 17, "name": "寒露", "title": "寒露 · 菊有黄华", "features": "傲霜初绽的金黄秋菊、渐冷秋水与飘零落叶", "keywords": ["菊华", "冷露", "深秋"], "season": "秋", "colors": "炭黑 · 菊黄 · 深褐", "output": "images/solar_terms/17_寒露.png"},
    {"id": 18, "name": "霜降", "title": "霜降 · 豺乃祭兽", "features": "枝头挂满红彤彤甜柿、薄霜覆盖草木与红枫", "keywords": ["柿红", "初霜", "晚秋"], "season": "秋", "colors": "炭黑 · 柿红 · 霜蓝灰", "output": "images/solar_terms/18_霜降.png"},
    {"id": 19, "name": "立冬", "title": "立冬 · 水始冰", "features": "初冬水面结薄冰、落木萧萧与归仓粮囤", "keywords": ["水始冰", "敛藏", "初冬"], "season": "冬", "colors": "炭黑 · 赭石 · 冰蓝", "output": "images/solar_terms/19_立冬.png"},
    {"id": 20, "name": "小雪", "title": "小雪 · 虹藏不见", "features": "漫天飞舞初雪微落、傲立寒风的蜡梅花苞", "keywords": ["微雪", "蜡梅", "清寒"], "season": "冬", "colors": "炭黑 · 蜡梅黄 · 雪青", "output": "images/solar_terms/20_小雪.png"},
    {"id": 21, "name": "大雪", "title": "大雪 · 鹖鴠不鸣", "features": "银装素裹的松柏雪挂、深山积雪小径与寒鸦", "keywords": ["千山雪", "松柏", "至寒"], "season": "冬", "colors": "炭黑 · 松绿 · 冷灰", "output": "images/solar_terms/21_大雪.png"},
    {"id": 22, "name": "冬至", "title": "冬至 · 蚯蚓结", "features": "红泥小火炉升腾热气、一枝红梅与窗外飞雪", "keywords": ["日南至", "围炉", "数九"], "season": "冬", "colors": "炭黑 · 炉火红 · 冷灰", "output": "images/solar_terms/22_冬至.png"},
    {"id": 23, "name": "小寒", "title": "小寒 · 雁北乡", "features": "严寒枝头盛放红梅、喜鹊立于积雪梅枝迎风", "keywords": ["鹊筑巢", "腊梅", "岁暮"], "season": "冬", "colors": "炭黑 · 梅红 · 深褐", "output": "images/solar_terms/23_小寒.png"},
    {"id": 24, "name": "大寒", "title": "大寒 · 鸡始乳", "features": "岁暮坚冰、迎春松柏红梅与瑞雪待迎新春", "keywords": ["坚冰", "瑞雪", "除旧迎新"], "season": "冬", "colors": "炭黑 · 朱红 · 松绿", "output": "images/solar_terms/24_大寒.png"},
]

collections = {
    "cities": {
        "id": "cities",
        "title": "世界城市",
        "titleEn": "World Cities",
        "count": len(cities_items),
        "kicker": "field notes / rubber stamp travel posters / 2026",
        "headline": "橡胶戳旅行实地笔记<br>世界城市",
        "desc": "30 座城市，30 枚低调的多色橡胶戳。每一张只留下一个地点最易辨认的轮廓：建筑、山脉、海岸线与城市的呼吸。",
        "tagPrefix": "NO.",
        "badgeFormat": "NO. {id}",
        "items": cities_items
    },
    "zodiac": {
        "id": "zodiac",
        "title": "十二生肖",
        "titleEn": "Chinese Zodiac",
        "count": len(zodiac_items),
        "kicker": "chinese zodiac / rubber stamp series / 2026",
        "headline": "橡胶戳印灵兽志<br>十二生肖",
        "desc": "12 种生肖瑞兽，12 幅质朴的纯粹手工橡胶戳印。剥离所有文字与排版干扰，仅以多色印章木版雕刻质感呈现动物的灵动神韵。",
        "tagPrefix": "生肖",
        "badgeFormat": "生肖 {id}",
        "items": zodiac_items
    },
    "solar_terms": {
        "id": "solar_terms",
        "title": "二十四节气",
        "titleEn": "24 Solar Terms",
        "count": len(solar_items),
        "kicker": "24 solar terms / seasonal stamp prints / 2026",
        "headline": "橡胶戳时序物候<br>二十四节气",
        "desc": "春生、夏长、秋收、冬藏。24 个节气，24 帧凝结于陈旧米白宣纸上的时序物候印记。去尽铅华文字，唯留四时风物之美。",
        "tagPrefix": "节气",
        "badgeFormat": "节气 {id}",
        "items": solar_items
    }
}

output_js = f"""// 橡胶戳艺术画廊数据集：世界城市 (30) · 十二生肖 (12) · 二十四节气 (24)
window.COLLECTIONS = {json.dumps(collections, ensure_ascii=False, indent=2)};

// 兼容旧版引用
window.CITIES = window.COLLECTIONS.cities.items;
window.ZODIAC = window.COLLECTIONS.zodiac.items;
window.SOLAR_TERMS = window.COLLECTIONS.solar_terms.items;
"""

(BASE / "data.js").write_text(output_js, encoding="utf-8")
print(f"data.js updated successfully! Collections: cities({len(cities_items)}), zodiac({len(zodiac_items)}), solar_terms({len(solar_items)})")
