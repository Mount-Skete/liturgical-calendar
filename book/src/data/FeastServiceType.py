class FeastServiceType:

    @staticmethod
    def from_type_rank(type: str, rank: str):
        # https://azbyka.ru/days/p-znaki-prazdnikov
        result = ''
        if rank == 'vigil' and type == 'great':
            result = b'\\U0001f540'  # 🕀
        elif rank == 'vigil' and type == 'middle':
            result = b'\\U0001f541'  # 🕁
        elif rank == 'polyeleos' and type == 'middle':
            result = b'\\U0001f542'  # 🕂
        elif (rank == 'great_doxology' or rank == 'six_stichera') and type == 'middle':
            result = b'\\U0001f543'  # 🕃

        if result == '':
            return result

        return (result
                .decode('unicode_escape')
                .encode('ascii', 'xmlcharrefreplace')
                .decode())

    @staticmethod
    def from_symbol(symbol: str, is_highlighted: bool):
        char_code = symbol.strip().encode('unicode_escape')

        if char_code == b'\\U0001f540':
            pass
            # return self.ServiceType(
            #     name='Typikon Symbol Great Feast',
            #     is_red=is_red,
            #     rank='vigil',
            #     type='great'
            # )
        elif char_code == b'\\U0001f541':
            pass
            # return self.ServiceType(
            #     name='Typikon Symbol Vigil Service',
            #     is_red=is_red,
            #     rank='vigil',
            #     type='middle'
            # )
        elif char_code == b'\\U0001f542':
            pass
            # return self.ServiceType(
            #     name='Typikon Symbol Polyeleos',
            #     is_red=is_red,
            #     rank='polyeleos',
            #     type='middle'
            # )
        elif char_code == b'\\U0001f543':
            pass
            # return self.ServiceType(
            #     name='Typikon Symbol Lower Rank',
            #     is_red=is_red,
            #     rank='great_doxology' if is_red else 'six stichera',
            #     type='middle'
            # )

        raise NotImplementedError(f'Service char {char_code} is not recognised')
