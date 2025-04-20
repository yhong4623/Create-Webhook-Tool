_category_id = None

def set_category_id(category_id: int):
    """設置全局類別 ID"""
    global _category_id
    _category_id = category_id

def get_category_id() -> int:
    """獲取全局類別 ID"""
    return _category_id