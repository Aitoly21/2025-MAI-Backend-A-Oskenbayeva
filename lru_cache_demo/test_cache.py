from cache import LRUCache

def main():
    cache = LRUCache(3)
    cache.set('Lipstick', 'Red Ruby')
    cache.set('Foundation', 'Matte Beige')
    cache.set('Mascara', 'Volume Boost')
    
    # Обновим значение помады
    cache.set('Lipstick', 'Coral Charm')
    print(cache.get('Lipstick'))  # Ожидаем 'Coral Charm'

    # Удалим тональник
    cache.rem('Foundation')
    print(cache.get('Foundation'))  # Ожидаем ''

if __name__ == "__main__":
    main()

