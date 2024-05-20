import math 
""" math 모듈의 PI와 sqrt를 사용하기 위해 모듈 불러오기"""

class Line: 
    """길이를 나타내는 Line 클래스 설정"""
    
    def __init__(self, length=1):
        """
        Line 클래스의 생성자로 초기 길이를 설정
        기본값은 1
        길이가 int 또는 float이 아니거나 0 이하인 경우 기본값 1을 설정
        """
        if not isinstance(length, (int, float)) or length <= 0:
            self.__length = 1
        else:
            self.__length = length

    def set_length(self, length):
        """
        길이를 설정하는 함수
        입력된 값이 int 또는 float 타입이고, 0보다 큰 경우에만 길이를 설정
        Args: length
            length (int or float): 설정할 길이 값
        """
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length
        else:
            return

    def get_length(self):
        """
        길이를 반환하는 함수
        Returns: 
            length 속성값을 반환
        """
        return self.__length
    
def area_square(line):
     """
        정사각형의 넓이를 계산하는 함수
        Args: line
            line (int or float): Line 클래스의 객체
        Returns: 
            정사각형의 넓이를 반환
     """
     if not isinstance(line, Line):
        return 0
     return line.get_length() ** 2

def area_circle(line):
        """
        원의 넓이를 계산하는 함수
        Args: 
            line (int or float): Line 클래스의 객체
        Returns: 
            원의 넓이를 반환
        """
        if not isinstance(line, Line):
            return 0
        return line.get_length() ** 2 * math.pi

def area_regular_triangle(line):
        """
        정삼각형의 넓이를 계산하는 함수
        Args: 
            line (int or float): Line 클래스의 객체
        Returns: 
            정삼각형의 넓이를 반환
        """
        if not isinstance(line, Line):
            return 0
        return line.get_length() ** 2 * math.sqrt(3) / 4