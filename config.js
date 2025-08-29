/**
 * 产品广告生成器配置文件
 * Product Ad Generator Configuration
 */

const CONFIG = {
    // API 配置
    API: {
        // Gemini API 基础 URL
        BASE_URL: 'https://generativelanguage.googleapis.com/v1beta',
        
        // 使用的模型版本
        MODEL: 'gemini-2.0-flash-exp',
        
        // 请求超时时间（毫秒）
        TIMEOUT: 30000,
        
        // 重试配置
        RETRY: {
            MAX_ATTEMPTS: 3,
            INITIAL_DELAY: 1000,
            BACKOFF_MULTIPLIER: 2
        }
    },

    // 图片配置
    IMAGE: {
        // 支持的文件格式
        SUPPORTED_FORMATS: ['image/png', 'image/jpeg', 'image/webp'],
        
        // 最大文件大小（字节）
        MAX_SIZE: 4 * 1024 * 1024, // 4MB
        
        // 推荐尺寸
        RECOMMENDED_SIZE: {
            WIDTH: 1024,
            HEIGHT: 1024
        }
    },

    // 广告场景配置
    AD_FORMATS: [
        {
            id: 'billboard',
            name: '城市广告牌',
            description: '繁华城市中心如时代广场的巨型广告牌',
            prompt: 'A massive billboard in a bustling city center like Times Square',
            category: 'outdoor'
        },
        {
            id: 'magazine',
            name: '杂志广告',
            description: '时尚杂志的全页彩色广告',
            prompt: 'A full-page color advertisement in a glossy fashion magazine',
            category: 'print'
        },
        {
            id: 'bus',
            name: '公交广告',
            description: '伦敦经典红色双层巴士侧面广告',
            prompt: 'An ad on the side of a classic red double-decker bus in London',
            category: 'transport'
        },
        {
            id: 'airport',
            name: '机场数字屏',
            description: '未来感机场航站楼的数字屏幕广告',
            prompt: 'A digital screen ad at a futuristic airport terminal',
            category: 'digital'
        },
        {
            id: 'coffeeshop',
            name: '咖啡店招牌',
            description: '鹅卵石街道上温馨咖啡店外的木质招牌',
            prompt: 'A rustic wooden sign outside a cozy coffee shop on a cobblestone street',
            category: 'retail'
        },
        {
            id: 'social',
            name: '社交媒体',
            description: '知名网红社交媒体动态中的赞助帖子',
            prompt: 'A social media sponsored post on a popular influencer\'s feed',
            category: 'digital'
        },
        {
            id: 'vintage_poster',
            name: '复古海报',
            description: '时尚小巷砖墙上的复古风格海报',
            prompt: 'A vintage-style poster on a brick wall in a trendy alleyway',
            category: 'street'
        },
        {
            id: 'jumbotron',
            name: '体育场大屏',
            description: '爆满体育场大屏幕上的广告',
            prompt: 'An advertisement on a jumbotron screen at a packed sports stadium',
            category: 'sports'
        },
        {
            id: 'movie_placement',
            name: '电影植入',
            description: '高预算电影场景中桌上的产品植入',
            prompt: 'A product placement on a table in a scene from a high-budget movie',
            category: 'entertainment'
        },
        {
            id: 'airplane_ad',
            name: '飞机座椅广告',
            description: '商用飞机座椅背面的广告',
            prompt: 'An ad on the back of a seat on a commercial airplane',
            category: 'transport'
        }
    ],

    // UI 配置
    UI: {
        // 主题配置
        THEME: {
            PRIMARY_COLOR: 'purple',
            SECONDARY_COLOR: 'pink',
            ACCENT_COLOR: 'blue'
        },
        
        // 动画配置
        ANIMATION: {
            DURATION: 300,
            EASING: 'ease-in-out'
        },
        
        // 响应式断点
        BREAKPOINTS: {
            SM: '640px',
            MD: '768px',
            LG: '1024px',
            XL: '1280px'
        }
    },

    // 本地存储键名
    STORAGE_KEYS: {
        API_KEY: 'gemini_api_key',
        THEME: 'app_theme',
        LAST_FORMAT: 'last_selected_format'
    },

    // 错误消息
    ERROR_MESSAGES: {
        NO_API_KEY: '请输入您的 Gemini API 密钥',
        NO_IMAGE: '请先上传产品图片',
        NO_FORMAT: '请选择广告格式',
        FILE_TOO_LARGE: '文件大小超过限制（最大 4MB）',
        UNSUPPORTED_FORMAT: '不支持的文件格式',
        API_ERROR: 'API 请求失败，请稍后重试',
        NETWORK_ERROR: '网络连接失败，请检查网络设置',
        GENERATION_FAILED: '广告生成失败，请尝试其他场景'
    },

    // 成功消息
    SUCCESS_MESSAGES: {
        IMAGE_UPLOADED: '图片上传成功',
        FORMAT_SELECTED: '广告格式已选择',
        GENERATION_COMPLETE: '广告生成完成',
        IMAGE_DOWNLOADED: '图片下载成功'
    }
};

// 导出配置（适用于模块化环境）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}

// 全局配置（适用于浏览器环境）
if (typeof window !== 'undefined') {
    window.APP_CONFIG = CONFIG;
}