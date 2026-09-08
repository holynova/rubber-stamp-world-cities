import json
from pathlib import Path

BASE = Path("/Users/sym/code/rubber-stamp-world-cities")

# 1. World Cities (30)
try:
    cities_items = json.loads((BASE / "prompts.json").read_text(encoding="utf-8"))
    for c in cities_items:
        if "prompt" in c:
            del c["prompt"]
except Exception:
    cities_items = []

# 2. Scenic Spots (50)
try:
    scenic_raw = json.loads((BASE / "prompts_scenic_spots.json").read_text(encoding="utf-8"))
    scenic_items = []
    for s in scenic_raw:
        item = {k: v for k, v in s.items() if k != "prompt"}
        scenic_items.append(item)
except Exception:
    scenic_items = []

# 3. Zodiac (12)
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

# 4. Solar Terms (24)
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

# 5. Shan Hai Jing (10)
shanhaijing_items = [
    {"id": 1, "name": "九尾狐", "title": "九尾狐 · 青丘瑞影", "features": "青丘九尾灵狐、摇曳祥云、仙雾缭绕、祥瑞灵动", "keywords": ["青丘", "九尾", "灵狐", "祥瑞"], "colors": "朱砂赤红 · 杏黄 · 宣纸暖米", "output": "images/shanhaijing/01_九尾狐.png"},
    {"id": 2, "name": "烛九阴", "title": "烛九阴 · 钟山昼夜", "features": "钟山之神烛龙、衔烛照幽、口吹冬夏、日月交错", "keywords": ["烛龙", "钟山", "昼夜", "神祇"], "colors": "赤红 · 宇宙靛蓝 · 砂金", "output": "images/shanhaijing/02_烛九阴.png"},
    {"id": 3, "name": "帝江", "title": "帝江 · 天山神舞", "features": "天山六足四翼神鸟、浑敦无面、知晓歌舞、浑然天成", "keywords": ["天山", "六足四翼", "歌舞", "浑敦"], "colors": "丹火红 · 姜黄 · 焦茶褐", "output": "images/shanhaijing/03_帝江.png"},
    {"id": 4, "name": "白泽", "title": "白泽 · 昆仑祥知", "features": "昆仑通万物神兽、避凶趋吉、仙松古石、浩然正气", "keywords": ["昆仑", "白泽", "辟邪", "知万物"], "colors": "石绿 · 翡翠青 · 暖赭", "output": "images/shanhaijing/04_白泽.png"},
    {"id": 5, "name": "毕方", "title": "毕方 · 丹水烈羽", "features": "独足神鹤、赤文青羽、衔火掠风、灵动不羁", "keywords": ["毕方", "独足", "神火", "青鹤"], "colors": "青金蓝 · 烈焰朱红 · 炭黑", "output": "images/shanhaijing/05_毕方.png"},
    {"id": 6, "name": "鲲鹏", "title": "鲲鹏 · 绝云扶摇", "features": "北冥巨鲲化鹏、翼若垂天、击水三千、扶摇直上", "keywords": ["北冥", "化鹏", "垂天之翼", "扶摇"], "colors": "普鲁士深蓝 · 浪花米白 · 暖金", "output": "images/shanhaijing/06_鲲鹏.png"},
    {"id": 7, "name": "饕餮", "title": "饕餮 · 青铜兽纹", "features": "商周青铜饕餮、威严兽面、双目如炬、吞天纳地", "keywords": ["饕餮", "青铜纹", "神威", "图腾"], "colors": "古青铜绿 · 赭石 · 炭墨", "output": "images/shanhaijing/07_饕餮.png"},
    {"id": 8, "name": "穷奇", "title": "穷奇 · 邽山风翼", "features": "飞翼神虎、凶猛矫健、御风疾行、啸傲崇山", "keywords": ["穷奇", "翼虎", "御风", "神煞"], "colors": "焦茶虎赤 · 墨黑 · 苍石灰", "output": "images/shanhaijing/08_穷奇.png"},
    {"id": 9, "name": "陆吾", "title": "陆吾 · 昆仑天守", "features": "昆仑山守宫神、虎身九尾、神圣威仪、镇守天门", "keywords": ["陆吾", "天守", "昆仑之丘", "九尾虎神"], "colors": "宫廷赭金 · 陶土朱红 · 翠玉", "output": "images/shanhaijing/09_陆吾.png"},
    {"id": 10, "name": "夫诸", "title": "夫诸 · 敖岸踏水", "features": "四角白鹿、凌波微步、引水润物、清灵绝尘", "keywords": ["夫诸", "四角白鹿", "踏水", "灵鹿"], "colors": "宣纸素白 · 远山淡黛 · 水蓝", "output": "images/shanhaijing/10_夫诸.png"},
]

# 6. Classical Chinese Poetry (50)
try:
    poetry_raw = json.loads((BASE / "prompts_poetry.json").read_text(encoding="utf-8"))
    poetry_items = []
    for p in poetry_raw:
        item = {
            "id": p["id"],
            "name": p["name"],
            "title": f"「{p['name']}」· {p['author']}{p['work']}",
            "verse": p["verse"],
            "author": p["author"],
            "dynasty": p["dynasty"],
            "work": p["work"],
            "category": p["category"],
            "features": f"「{p['verse']}」 {p['features']}",
            "keywords": p["keywords"],
            "colors": p["colors"],
            "output": p["output"]
        }
        poetry_items.append(item)
except Exception as e:
    print(f"Error loading poetry prompts: {e}")
    poetry_items = []

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
    "scenic_spots": {
        "id": "scenic_spots",
        "title": "名胜风景",
        "titleEn": "China 5A Scenic Spots",
        "count": len(scenic_items),
        "kicker": "china national scenic heritage / rubber stamp collection / 2026",
        "headline": "橡胶戳华夏胜景<br>中国 5A 级景区名胜",
        "desc": "精选 50 处中国最具代表性的 5A 级风景名胜与世界文化遗产。以极简手工线刻橡胶印章凝固华夏山河的壮丽画卷。",
        "tagPrefix": "胜景",
        "badgeFormat": "胜景 {id}",
        "items": scenic_items
    },
    "poetry": {
        "id": "poetry",
        "title": "古诗名句",
        "titleEn": "Classical Poetry",
        "count": len(poetry_items),
        "kicker": "classical chinese poetry / visual stamp prints / 2026",
        "headline": "橡胶戳诗意画境<br>古诗名句",
        "desc": "50 句极具画面感的中国经典古诗词，50 帧纯粹的手工多色线刻橡胶印章。以意入境、留白成趣，图章之下铭刻千古名句。",
        "tagPrefix": "诗词",
        "badgeFormat": "诗词 {id}",
        "items": poetry_items
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
    },
    "shanhaijing": {
        "id": "shanhaijing",
        "title": "山海神异",
        "titleEn": "Classic of Mountains & Seas",
        "count": len(shanhaijing_items),
        "kicker": "classic of mountains and seas / mythical beasts / 2026",
        "headline": "橡胶戳上古神祇<br>山海神异",
        "desc": "10 尊中国上古神话异兽与司天神祇。取材于《山海经》大荒经与海内经，以纯粹无文字的多色木刻雕版印章，重现九尾狐、烛九阴、帝江、白泽等上古神灵的奇崛神韵。",
        "tagPrefix": "神兽",
        "badgeFormat": "山海 {id}",
        "items": shanhaijing_items
    }
}

output_js = f"""// 橡胶戳艺术画廊数据集：世界城市 (30) · 名胜风景 (50) · 古诗名句 (50) · 十二生肖 (12) · 二十四节气 (24) · 山海神异 (10)
window.COLLECTIONS = {json.dumps(collections, ensure_ascii=False, indent=2)};

// 兼容旧版引用
window.CITIES = window.COLLECTIONS.cities.items;
window.SCENIC_SPOTS = window.COLLECTIONS.scenic_spots.items;
window.POETRY = window.COLLECTIONS.poetry.items;
window.ZODIAC = window.COLLECTIONS.zodiac.items;
window.SOLAR_TERMS = window.COLLECTIONS.solar_terms.items;
window.SHANHAIJING = window.COLLECTIONS.shanhaijing.items;
"""

(BASE / "data.js").write_text(output_js, encoding="utf-8")
print(f"data.js updated successfully! Total 6 collections: cities({len(cities_items)}), scenic({len(scenic_items)}), poetry({len(poetry_items)}), zodiac({len(zodiac_items)}), solar({len(solar_items)}), shj({len(shanhaijing_items)}) -> Total {len(cities_items) + len(scenic_items) + len(poetry_items) + len(zodiac_items) + len(solar_items) + len(shanhaijing_items)} stamps.")
