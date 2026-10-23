import tkinter as tk
import tkinter.font as tkfont
import random

message = [
    "答应过的事，阿英永不会变",
    "好好爱自己",
    "在我这里，永远娘子最大",
    "你是我最想见的人",
    "今天也是爱你的一天",
    "在你面前，阿英永远不会变",
    "长赢，阿英早已寻见那朵永不凋谢的花",
    "长赢，你是我戏里最美好的女主角",
    "这份爱，是我这出戏唯一的内核",
    "这就是小男孩生命里所有的真",
    "她是我唯一的理由，但我不必是她的唯一",
    "玄英为冬，长赢为夏，相隔春秋，此生无有相见",
    "她该去看看春莹，看看秋棠，还有夏雪与冬花",
    "我要给你一场绝无仅有的婚礼",
    "蒲公英会随风飘荡"
]

bg_colors = ["#C3C7CE", "#E2D8DB", "#E5DCD2", "#C2C9C0", "#F0EEE9", "#D6B9B3",
             "#F5DEB3", "#D8BFD8", "#B0E0E6", "#FFDAB9"]

POPUP_COUNT = 300  # 总共要弹出的窗口数量
GENERATE_INTERVAL = 60  # 每个弹窗生成的时间间隔（毫秒）

# 全部显示完后，窗口消失的时间范围（毫秒）
POPUP_DURATION_MIN = 0
POPUP_DURATION_MAX = POPUP_COUNT * 8

#边距设置
TOP_MARGIN = 20       # 距离屏幕顶部的边距
BOTTOM_MARGIN = 80   # 距离屏幕底部的边距
SIDE_MARGIN = 20      # 距离屏幕左右两侧的边距

# 用于存储所有弹窗的列表
all_popups = []


def create_popup(root):
    # 随机选择一条祝福语
    msg = random.choice(message)
    # 随机选择背景色
    bg = random.choice(bg_colors)
    # 字体大小
    font_size = 15
    #创建字体对象并测量文字宽度, family="" 表示使用系统默认字体
    custom_font = tkfont.Font(family="", size=font_size)
    text_width = custom_font.measure(msg)

    # 创建独立弹窗
    popup = tk.Toplevel(root)
    popup.title("阿英永远是阿英")
    popup.configure(bg=bg)

    #根据文字宽度计算弹窗大小，加上左右边距
    padding_x = 40  # 左右边距
    padding_y = 40  # 上下边距
    width = text_width + padding_x
    height = font_size + padding_y
    
    # 设置一个最小宽度，防止文字太短时窗口太丑
    if width < 120:
        width = 120

    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 水平位置计算（左右统一边距）
    min_x = SIDE_MARGIN
    max_x = screen_width - width - SIDE_MARGIN
    if max_x < min_x: max_x = min_x
    x = random.randint(min_x, max_x)

    # 垂直位置计算（上下分别设置边距）
    min_y = TOP_MARGIN
    max_y = screen_height - height - BOTTOM_MARGIN
    if max_y < min_y: max_y = min_y
    y = random.randint(min_y, max_y)

    # 设置窗口大小和位置
    popup.geometry(f"{width}x{height}+{x}+{y}")

    # 创建文字标签
    label = tk.Label(
        popup,
        text=msg,
        bg=bg,
        font=("", font_size)
    )
    label.pack(expand=True, fill="both")

    # 将弹窗加入列表
    all_popups.append(popup)


def start_disappearing(root):
    # 1. 让所有窗口开始随机消失
    for p in all_popups:
        delay = random.randint(POPUP_DURATION_MIN, POPUP_DURATION_MAX)
        p.after(delay, p.destroy)

    # 2. 计算程序退出的时间
    quit_delay = POPUP_DURATION_MAX + 500
    
    # 3. 设置定时器关闭主程序
    root.after(quit_delay, root.destroy)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    # 批量调度弹窗
    for i in range(POPUP_COUNT):
        root.after(i * GENERATE_INTERVAL, create_popup, root)

    # 计算全部弹窗生成完毕所需的总时间
    total_time = (POPUP_COUNT * GENERATE_INTERVAL) + 3000
    
    # 定时执行“开始消失”函数，并传入 root 参数
    root.after(total_time, start_disappearing, root)

    # 启动主循环
    root.mainloop()
