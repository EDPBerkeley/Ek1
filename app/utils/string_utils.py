
class StringUtils:
    @staticmethod
    def to_camel_case(s):
        words = s.split()
        return words[0].lower() + ''.join(word.capitalize() or '_' for word in words[1:])
