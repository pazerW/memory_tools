import random
from datetime import datetime
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
import io
import os

# 符号库用于抽象符号矩阵
SYMBOLS = ['△', '☆', '□', '♣', '♠', '★', '●', '■', '▲', '◆', '◐', '◑', '◒', '◓', '◔', '◕']

# 词库用于无序词对
NOUNS = ['量子', '熵', '混沌', '纳米', '基因', '拓扑', '函数', '算法', '神经网络', '宇宙', '弦论', '光合作用']
ADJECTIVES = ['超导', '递归', '分形', '量子化', '非线性', '全息', '拓扑', '混沌', '熵增', '相对论性', '基因编辑']

# 方向库用于动态路径
DIRECTIONS = ['↑', '↗', '→', '↘', '↓', '↙', '←', '↖']

# 声音库用于跨感官转换
SOUNDS = ['齿轮转动声', '水流声', '雷声', '鸟鸣声', '心跳声', '金属撞击声', '玻璃破碎声', '火焰燃烧声']

# 专业领域库
LEGAL_CONCEPTS = ['显失公平原则', '不当得利', '善意取得', '过错推定', '举证责任倒置']
MEDICAL_STRUCTURES = ['左心室', '肝右叶', '肾小球', '肺泡', '视神经', '海马体', '前额叶皮层']
FOREIGN_PHRASES = ['Poser un lapin', 'Coup de foudre', 'Schadenfreude', 'Wanderlust', 'Saudade']
FINANCIAL_MODELS = ['布莱克-舒尔斯模型', 'CAPM模型', '蒙特卡洛模拟', 'ARCH模型', '马尔可夫链']

def generate_daily_training(difficulty=3):
    """生成每日记忆力训练数据，包含数字记忆训练"""
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # 根据难度调整参数
    digit_length = difficulty * 15  # 数字串长度
    matrix_size = difficulty + 2   # 矩阵大小
    num_pairs = difficulty * 5     # 词对数量
    
    # 随机选择一种随机信息训练类型
    random_training_type = random.choice([
        "抽象符号矩阵", "无序词对联想", "多模态干扰序列", 
        "动态路径闪记", "跨感官转换", "数字串记忆", "二进制矩阵"
    ])
    
    # 随机选择一种特定技能领域
    skill_domain = random.choice(["法律", "医学", "外语", "金融"])
    # 生成随机数字串
    # 生成10的倍数长度的数字串，每组为2位（01-99），不足时补0
    num_pairs = 100
    digits = [f"{random.randint(1,99):02d}" for _ in range(num_pairs)]
    memory_numbers = {
        "type": random_training_type,
        "digits": digits,
        "time_limit": digit_length // 4  # 每4个数字1秒
    }
    # 生成随机信息训练数据
    if random_training_type == "抽象符号矩阵":
        size = random.randint(3, matrix_size)  # 矩阵大小
        matrix = [[random.choice(SYMBOLS) for _ in range(size)] for _ in range(size)]
        training_data = {
            "type": random_training_type,
            "content": matrix,
            "time_limit": max(5, size*2)  # 时间限制根据矩阵大小变化
        }
    
    elif random_training_type == "无序词对联想":
        num = random.randint(8, num_pairs)
        pairs = []
        for _ in range(num):
            # 确保词对没有逻辑关联
            word1 = random.choice(NOUNS)
            word2 = random.choice(ADJECTIVES)
            while word1 == word2:  # 防止相同词
                word2 = random.choice(ADJECTIVES)
            pairs.append((word1, word2))
        training_data = {
            "type": random_training_type,
            "content": pairs,
            "time_limit": num // 2  # 每对词0.5秒
        }
    
    elif random_training_type == "多模态干扰序列":
        length = random.randint(5, 10)
        numbers = [random.randint(0, 9) for _ in range(length)]
        colors = [random.choice(['🔴', '🟢', '🔵', '🟡', '🟣']) for _ in range(length)]
        training_data = {
            "type": random_training_type,
            "audio": numbers,
            "visual": colors,
            "time_limit": length // 2  # 每项0.5秒
        }
    
    elif random_training_type == "动态路径闪记":
        path_length = random.randint(6, 12)
        path = [random.choice(DIRECTIONS) for _ in range(path_length)]
        training_data = {
            "type": random_training_type,
            "path": path,
            "time_limit": path_length // 3  # 每方向约0.3秒
        }
    
    # elif random_training_type == "数字串记忆":
    #     # 生成随机数字串
    #     digits = ''.join(str(random.randint(0, 9)) for _ in range(digit_length))
    #     training_data = {
    #         "type": random_training_type,
    #         "digits": digits,
    #         "time_limit": digit_length // 4  # 每4个数字1秒
    #     }
    
    elif random_training_type == "二进制矩阵":
        size = random.randint(4, 6)
        matrix = [[str(random.randint(0, 1)) for _ in range(size)] for _ in range(size)]
        training_data = {
            "type": random_training_type,
            "content": matrix,
            "time_limit": size * 2  # 时间限制根据矩阵大小变化
        }
    
    else:  # 跨感官转换
        sound = random.choice(SOUNDS)
        training_data = {
            "type": random_training_type,
            "sound": sound,
            "time_limit": 5  # 5秒时间
        }
    
    # 生成特定技能深化数据
    if skill_domain == "法律":
        concept = random.choice(LEGAL_CONCEPTS)
        elements = random.sample(['主体资格', '主观意图', '客观行为', '因果关系', '损害结果'], k=random.randint(3, 5))
        exceptions = random.choice(['商事主体除外', '紧急避险情形', '不可抗力因素'])
        skill_data = {
            "domain": skill_domain,
            "concept": concept,
            "elements": elements,
            "exceptions": exceptions
        }
    
    elif skill_domain == "医学":
        structure = random.choice(MEDICAL_STRUCTURES)
        functions = random.sample(['物质运输', '信号传导', '能量转换', '信息处理', '结构支持'], k=random.randint(1, 3))
        pathologies = random.sample(['炎症', '肿瘤', '变性', '坏死', '萎缩'], k=random.randint(1, 2))
        skill_data = {
            "domain": skill_domain,
            "structure": structure,
            "functions": functions,
            "pathologies": pathologies
        }
    
    elif skill_domain == "外语":
        phrase = random.choice(FOREIGN_PHRASES)
        meaning = random.choice(['放鸽子', '一见钟情', '幸灾乐祸', '旅行癖', '乡愁'])
        traps = random.choice(['不可直译', '仅限口语', '含贬义', '地域性用语'])
        skill_data = {
            "domain": skill_domain,
            "phrase": phrase,
            "meaning": meaning,
            "traps": traps
        }
    
    else:  # 金融
        model = random.choice(FINANCIAL_MODELS)
        variables = random.sample(['σ', 'r', 'μ', 'β', 'α', 'λ'], k=random.randint(2, 4))
        event = random.choice(['2020年3月波动率飙升', '2008年次贷危机', '2015年A股熔断'])
        skill_data = {
            "domain": skill_domain,
            "model": model,
            "variables": variables,
            "event": event
        }
    
    return {
        "date": date_str,
        "memory_numbers": memory_numbers,
        "random_training": training_data,
        "skill_training": skill_data,
        "difficulty": difficulty
    }

def print_training(training):
    """格式化打印训练数据"""
    print(f"\n=== 每日记忆力训练 {training['date']} (难度: {training['difficulty']}/5) ===")
    
    print("\n[数字记忆训练]")
    digits = training['memory_numbers']['digits']
    time_limit = training['memory_numbers']['time_limit']
    # 每10位为一行打印数字串
    print("数字串:")
    for i in range(0, len(digits), 10):
        print(" ".join(digits[i:i+10]))
    print(f"(限时: {time_limit}秒)")
    print(f"长度: {len(digits)}位")
    
    # 打印随机信息训练
    rt = training['random_training']
    print(f"\n[随机信息即时记忆] - {rt['type']} (限时: {rt['time_limit']}秒)")
    
    if rt['type'] == "抽象符号矩阵":
        for row in rt['content']:
            print(" ".join(row))
    elif rt['type'] == "无序词对联想":
        for i, (word1, word2) in enumerate(rt['content']):
            print(f"{i+1}. {word1} - {word2}")
    elif rt['type'] == "多模态干扰序列":
        print(f"听觉序列: {', '.join(map(str, rt['audio']))}")
        print(f"视觉序列: {' '.join(rt['visual'])}")
    elif rt['type'] == "动态路径闪记":
        print("路径: " + " → ".join(rt['path']))
    elif rt['type'] == "数字串记忆":
        print(f"数字串: {rt['digits']}")
        print(f"长度: {len(rt['digits'])}位")
    elif rt['type'] == "二进制矩阵":
        for row in rt['content']:
            print(" ".join(row))
    else:  # 跨感官转换
        print(f"声音描述: {rt['sound']}")
        print("请转换为你的110编码")
    
    # 打印特定技能训练
    st = training['skill_training']
    print(f"\n[特定技能深化] - {st['domain']}领域")
    
    if st['domain'] == "法律":
        print(f"法律概念: {st['concept']}")
        print(f"核心要件: {', '.join(st['elements'])}")
        print(f"例外情形: {st['exceptions']}")
    elif st['domain'] == "医学":
        print(f"解剖结构: {st['structure']}")
        print(f"生理功能: {', '.join(st['functions'])}")
        print(f"病理变化: {', '.join(st['pathologies'])}")
    elif st['domain'] == "外语":
        print(f"外语短语: {st['phrase']}")
        print(f"中文含义: {st['meaning']}")
        print(f"使用陷阱: {st['traps']}")
    else:  # 金融
        print(f"金融模型: {st['model']}")
        print(f"关键变量: {', '.join(st['variables'])}")
        print(f"市场事件: {st['event']}")
    
    print("\n训练提示:")
    print("- 随机信息训练: 使用记忆宫殿快速编码，完成后立即回忆")
    print("- 技能深化训练: 将概念分解为要素，构建动态关联图像")
    print("- 记录主观编码难度(1-10分)和回忆准确率")
    
    # 添加数字记忆训练提示
    if rt['type'] in ["数字串记忆", "二进制矩阵"]:
        print("\n数字记忆技巧:")
        print("1. 使用你的110编码库将数字转换为图像")
        print("2. 将图像放置在记忆宫殿的特定位置")
        print("3. 对于长数字串，每3-4位数字创建一个复合图像")
        print("4. 二进制矩阵可视为黑白图像进行整体记忆")

def create_pdf(training, filename="memory_training.pdf"):
    """创建PDF格式的训练计划"""

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=72, leftMargin=72,
        topMargin=72, bottomMargin=18
    )
    # pdfmetrics.registerFont(TTFont('SimSun', 'SimSun.ttf'))
    pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=1,fontName='STSong-Light'))
    styles.add(ParagraphStyle(name='MyTitle', fontSize=16, alignment=1, spaceAfter=12,fontName='STSong-Light'))
    styles.add(ParagraphStyle(name='Subtitle', fontSize=14, textColor=colors.darkblue, spaceAfter=6,fontName='STSong-Light'))
    styles.add(ParagraphStyle(name='Heading', fontSize=12, textColor=colors.darkblue, spaceAfter=6,fontName='STSong-Light'))
    styles.add(ParagraphStyle(name='Body', fontSize=10, spaceAfter=6,fontName='STSong-Light'))
    styles.add(ParagraphStyle(name='Tip', fontSize=10, textColor=colors.darkgreen, spaceAfter=6,fontName='STSong-Light'))
    styles.add(ParagraphStyle(name='Number', fontSize=14, textColor=colors.darkgreen, spaceAfter=6,fontName='STSong-Light'))
    
    story = []
    
    # 标题
    title = f"记忆力训练计划 - {training['date']} (难度: {training['difficulty']}/5)"
    story.append(Paragraph(title, styles["MyTitle"]))
    story.append(Spacer(1, 12))
    
    # 数字记忆训练部分
    # 原始数据
    digits = training['memory_numbers']['digits']
    time_limit = training['memory_numbers']['time_limit']

    story.append(Paragraph("数字记忆训练:", styles["Subtitle"]))
    story.append(Paragraph(f"数字串 (长度: {len(digits)}位):", styles["Body"]))

    # 创建表格布局的数字串 (每10位一行)
    digit_lines = [digits[i:i+10] for i in range(0, len(digits), 10)]

    # 确保每行都有10个元素
    max_cols = 10
    
    for line in digit_lines:
        table_data = []
        row = list(line)
        # 填充不足的列
        if len(row) < max_cols:
            row += [''] * (max_cols - len(row))
        table_data.append(row)
        # 在每行后面插入一行空行
        # 获取实际行数
        num_rows = len(table_data)

        # 创建表格
        t = Table(table_data, 
                colWidths=[50] * max_cols,
                rowHeights=[25] * num_rows)

        # 设置表格样式
        t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('FONTSIZE', (0,0), (-1,-1), 14),
            ('FONTNAME', (0,0), (-1,-1), 'Courier'),
            ('LINEBELOW', (0,0), (-1,-1), 1, colors.grey),
            ('BOX', (0,0), (-1,-1), 1, colors.grey),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('GRID', (0,0), (-1,-1), 1, colors.grey), 
        ]))

        story.append(t)  # 添加表格到文档
        story.append(Spacer(1, 6))
        
    story.append(Spacer(3, 6))
    story.append(Paragraph(f"限时: {time_limit}秒", styles["Body"]))
    story.append(Spacer(1, 12))
    
    # 随机信息训练部分
    rt = training['random_training']
    story.append(Paragraph(f"随机信息即时记忆: {rt['type']}", styles["Subtitle"]))
    story.append(Paragraph(f"限时: {rt['time_limit']}秒", styles["Body"]))
    story.append(Spacer(1, 6))
    
    if rt['type'] == "抽象符号矩阵":
        data = rt['content']
        table = Table(data)
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'Helvetica', 14),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        story.append(table)
        
    elif rt['type'] == "无序词对联想":
        data = [["序号", "词对"]] + [[f"{i+1}.", f"{word1} - {word2}"] for i, (word1, word2) in enumerate(rt['content'])]
        table = Table(data, colWidths=[0.8*inch, 4*inch])
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'STSong-Light', 10),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            
        ]))
        story.append(table)
        
    elif rt['type'] == "多模态干扰序列":
        story.append(Paragraph(f"<b>听觉序列:</b> {', '.join(map(str, rt['audio']))}", styles["Body"]))
        story.append(Paragraph(f"<b>视觉序列:</b> {' '.join(rt['visual'])}", styles["Body"]))
        
    elif rt['type'] == "动态路径闪记":
        story.append(Paragraph(f"路径: {' → '.join(rt['path'])}", styles["Body"]))
        
    # elif rt['type'] == "数字串记忆":
    #     story.append(Paragraph(f"数字串 (长度: {len(rt['digits'])}位):", styles["Body"]))
    #     story.append(Paragraph(f"<font size=14>{rt['digits']}</font>", styles["Body"]))
    #     story.append(Spacer(1, 12))
    #     story.append(Paragraph("记忆提示:", styles["Heading"]))
    #     story.append(Paragraph("• 使用110编码将数字转换为图像", styles["Body"]))
    #     story.append(Paragraph("• 将图像放置在记忆宫殿中", styles["Body"]))
    #     story.append(Paragraph("• 对于长数字串，每3-4位创建一个复合图像", styles["Body"]))
        
    elif rt['type'] == "二进制矩阵":
        data = rt['content']
        table = Table(data)
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'Courier', 14),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 0), (-1, -1), colors.white)
        ]))
        story.append(table)
        story.append(Spacer(1, 6))
        story.append(Paragraph("记忆提示:", styles["Heading"]))
        story.append(Paragraph("• 将0视为白色方块，1视为黑色方块", styles["Body"]))
        story.append(Paragraph("• 寻找矩阵中的模式或形状", styles["Body"]))
        story.append(Paragraph("• 按行或列分组记忆", styles["Body"]))
        
    else:  # 跨感官转换
        story.append(Paragraph(f"声音描述: {rt['sound']}", styles["Body"]))
        story.append(Paragraph("请转换为你的110编码", styles["Body"]))
    
    story.append(Spacer(1, 18))
    
    # 特定技能训练部分
    st = training['skill_training']
    story.append(Paragraph(f"特定技能深化: {st['domain']}领域", styles["Subtitle"]))
    
    if st['domain'] == "法律":
        story.append(Paragraph(f"<b>法律概念:</b> {st['concept']}", styles["Body"]))
        story.append(Paragraph(f"<b>核心要件:</b> {', '.join(st['elements'])}", styles["Body"]))
        story.append(Paragraph(f"<b>例外情形:</b> {st['exceptions']}", styles["Body"]))
        
    elif st['domain'] == "医学":
        story.append(Paragraph(f"<b>解剖结构:</b> {st['structure']}", styles["Body"]))
        story.append(Paragraph(f"<b>生理功能:</b> {', '.join(st['functions'])}", styles["Body"]))
        story.append(Paragraph(f"<b>病理变化:</b> {', '.join(st['pathologies'])}", styles["Body"]))
        
    elif st['domain'] == "外语":
        story.append(Paragraph(f"<b>外语短语:</b> {st['phrase']}", styles["Body"]))
        story.append(Paragraph(f"<b>中文含义:</b> {st['meaning']}", styles["Body"]))
        story.append(Paragraph(f"<b>使用陷阱:</b> {st['traps']}", styles["Body"]))
        
    else:  # 金融
        story.append(Paragraph(f"<b>金融模型:</b> {st['model']}", styles["Body"]))
        story.append(Paragraph(f"<b>关键变量:</b> {', '.join(st['variables'])}", styles["Body"]))
        story.append(Paragraph(f"<b>市场事件:</b> {st['event']}", styles["Body"]))
    
    story.append(Spacer(1, 18))
    
    # 训练提示部分
    story.append(Paragraph("训练提示:", styles["Subtitle"]))
    story.append(Paragraph("- 随机信息训练: 使用记忆宫殿快速编码，完成后立即回忆", styles["Tip"]))
    story.append(Paragraph("- 技能深化训练: 将概念分解为要素，构建动态关联图像", styles["Tip"]))
    story.append(Paragraph("- 记录主观编码难度(1-10分)和回忆准确率", styles["Tip"]))
    
    # 添加数字记忆训练提示
    if rt['type'] in ["数字串记忆", "二进制矩阵"]:
        story.append(Spacer(1, 6))
        story.append(Paragraph("数字记忆技巧:", styles["Heading"]))
        story.append(Paragraph("1. 使用你的110编码库将数字转换为图像", styles["Tip"]))
        story.append(Paragraph("2. 将图像放置在记忆宫殿的特定位置", styles["Tip"]))
        story.append(Paragraph("3. 对于长数字串，每3-4位数字创建一个复合图像", styles["Tip"]))
        story.append(Paragraph("4. 二进制矩阵可视为黑白图像进行整体记忆", styles["Tip"]))
    
    # 创建PDF文档
    doc.build(story)
    print(f"\nPDF文件已生成: {filename}")
    return filename

def generate_and_save_training(difficulty=3):
    """生成训练内容并保存为PDF"""
    training = generate_daily_training(difficulty)
    # print_training(training)
    
    # 创建PDF文件名
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"memory_training_{date_str}_lv{difficulty}.pdf"
    
    # 生成PDF
    pdf_path = create_pdf(training, filename)
    
    # 尝试打开PDF文件
    try:
        os.startfile(pdf_path)  # Windows
    except:
        try:
            os.system(f'open "{pdf_path}"')  # macOS
        except:
            try:
                os.system(f'xdg-open "{pdf_path}"')  # Linux
            except:
                print(f"无法自动打开PDF，请手动打开文件: {pdf_path}")
    
    return training

# 生成并保存今日训练
if __name__ == "__main__":
    print("===== 记忆力训练生成器 =====")
    print("请选择难度级别 (1-5, 默认3):")
    difficulty = input("难度: ") or "3"
    
    try:
        difficulty = int(difficulty)
        if difficulty < 1: difficulty = 1
        if difficulty > 5: difficulty = 5
    except:
        difficulty = 3
    
    print(f"\n生成难度级别 {difficulty} 的训练内容...")
    generate_and_save_training(difficulty)