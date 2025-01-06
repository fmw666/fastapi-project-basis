class ErrorCode:
    """错误码定义
    命名规则：
    1. 前三位为 http 状态码
    2. 中间两位为模块 id
    3. 最后两位为序号

    注意：模块为 00 代表通用，序号为 00 代表模块中通用
    """

    # 通用错误码
    INTERNAL_SERVER_ERROR = 5000000
    BAD_REQUEST = 4000000
    UNAUTHORIZED = 4010000
    FORBIDDEN = 4030000
    NOT_FOUND = 4040000

    # 用户类 01
    USER_ERROR = 4000100
    USER_EXIST = 4000101
    USER_NOT_FOUND = 4040102
    USER_NAME_EXIST = 4000103
    USER_PASSWORD_ERROR = 4000104
    USER_EMAIL_EXIST = 4000105
    USER_SMS_CODE_ERROR = 4000106
    USER_PHONE_INVALID = 4000107
    USER_SMS_CODE_REQUEST_TOO_OFTEN = 4290108
    USER_UNAUTHORIZED = 4010109

    # ...