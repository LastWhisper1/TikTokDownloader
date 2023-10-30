# from random import randint
# from time import sleep

__all__ = [
    "MAX_WORKERS",
    "wait",
    "failed",
    "illegal_nickname",
    "check_login",
    "DESCRIPTION_LENGTH",
    "TEXT_REPLACEMENT",
    "conditional_filtering",
    "SERVER_HOST",
    "SERVER_PORT",
    "MASTER",
    "PROMPT",
    "WARNING",
    "ERROR",
    "INFO",
    "GENERAL",
    "PROGRESS",
    "rest",
    "COOKIE_UPDATE_INTERVAL",
]

# 线程池最大线程数量，多线程下载文件时使用
# 短期大批量下载文件可以适当设置更大的值
# 长期大批量下载文件不建议设置过大的值，可能会导致下载无响应（可能是抖音端风控）
MAX_WORKERS = 4

# 作品描述最大长度限制，仅对作品文件名称生效，不影响数据储存，设置时需要考虑系统文件名称最大长度限制
DESCRIPTION_LENGTH = 64

# 非法字符替换规则，key 为替换前的文本，value 为替换后的文本
TEXT_REPLACEMENT = {
    " ": " ",
}

# 服务器模式主机，设置为 0.0.0.0 可以实现局域网访问（外部可用）
SERVER_HOST = "127.0.0.1"

# 服务器模式端口
SERVER_PORT = 5000

# Cookie 更新间隔，单位：秒
COOKIE_UPDATE_INTERVAL = 15 * 60

# 彩色交互提示颜色设置，支持标准颜色名称、Hex、RGB 格式
MASTER = "b #fff200"
PROMPT = "b turquoise2"
GENERAL = "b bright_white"
PROGRESS = "b bright_magenta"
ERROR = "b bright_red"
WARNING = "b bright_yellow"
INFO = "b bright_green"


def wait():
    """
    设置网络请求间隔时间，仅对获取数据生效，不影响下载文件
    启用延迟需要将第 1 ~ 2 行代码取消注释
    """
    # 随机延时
    # sleep(randint(15, 35) * 0.1)
    # 固定延时
    # sleep(2)
    # 取消延时
    pass


def failed():
    """获取数据失败时，是否继续执行"""
    # 询问用户
    return input("输入任意字符继续运行，直接回车结束运行: ")
    # 继续执行
    # return True
    # 结束执行
    # return False


def illegal_nickname():
    """当 账号昵称/标识 或者 合集标题/标识 过滤非法字符后不是有效的文件夹名称时，如何处理异常"""
    # 询问用户
    return input("当前 账号昵称/标识 或者 合集标题/标识 不是有效的文件夹名称，请输入临时的账号标识或者合集标识：")
    # 使用当前时间戳作为账号昵称/标识或者合集标题/标识
    # return str(time())[:10]


def check_login():
    """扫描二维码登录账号时，是否询问用户再进行登录结果检查"""
    # 询问用户
    return input("是否已完成扫码登录？直接回车开始检查登录结果，输入任何字符放弃操作：")
    # 直接检查
    # return False


def conditional_filtering(data: list[dict]) -> list[dict]:
    """自定义作品筛选规则，例如：筛选作品点赞数、作品类型、视频分辨率等"""
    return data


def rest(count: int, screen):
    """
    如需采集大量账号数据，请启用该函数，可以在处理指定数量的账号后，暂停一段时间，然后继续运行
    batches: 每次处理的账号数量上限，比如：每次处理 10 个账号，就会暂停程序
    rest_time: 程序暂停的时间，单位：秒；比如：每处理 10 个账号，就暂停 10 分钟
    启用该函数需要将第 2 行代码取消注释
    仅对终端命令行模式的批量下载账号作品模式生效
    """
    # 启用该函数
    # batches = 10  # 根据实际需求修改
    # if not count % batches:
    #     rest_time = 60 * 10  # 根据实际需求修改
    #     screen(
    #         f"程序已经处理了 {batches} 个账号，为了避免请求频率过高导致账号或 IP 被风控，程序已经暂停，"
    #         f"在 {rest_time} 秒后继续处理账号！", style=GENERAL)
    #     sleep(rest_time)
    # 默认不启用
    pass
