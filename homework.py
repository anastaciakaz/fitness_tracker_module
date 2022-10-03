from dataclasses import dataclass, asdict
from typing import ClassVar


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    MESSAGE: ClassVar[str] = ('Тип тренировки: {training_type}; '
                              'Длительность: {duration:.3f} ч.; '
                              'Дистанция: {distance:.3f} км; '
                              'Ср. скорость: {speed:.3f} км/ч; '
                              'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        return self.MESSAGE.format(**asdict(self))


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: ClassVar[float] = 0.65
    M_IN_KM: ClassVar[int] = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance: float = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed: float = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info_message: InfoMessage = InfoMessage(self.__class__.__name__,
                                                self.duration,
                                                self.get_distance(),
                                                self.get_mean_speed(),
                                                self.get_spent_calories())
        return info_message


class Running(Training):
    """Тренировка: бег."""
    COEF_CALORIE_1: ClassVar[int] = 18
    COEF_CALORIE_2: ClassVar[int] = 20

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        spent_calories = ((self.COEF_CALORIE_1
                          * self.get_mean_speed()
                          - self.COEF_CALORIE_2)
                          * self.weight
                          / self.M_IN_KM
                          * (self.duration * 60))
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    COEF_CALORIE_3: ClassVar[float] = 0.035
    COEF_CALORIE_4: ClassVar[float] = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height: float = height

    def get_spent_calories(self) -> float:
        spent_calories = ((self.COEF_CALORIE_3
                          * self.weight
                          + (self.get_mean_speed()**2 // self.height)
                          * self.COEF_CALORIE_4
                          * self.weight)
                          * (self.duration * 60))
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: ClassVar[float] = 1.38
    COEF_CALORIE_5: ClassVar[float] = 1.1
    COEF_CALORIE_6: ClassVar[int] = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool: float = length_pool
        self.count_pool: float = count_pool

    def get_mean_speed(self) -> float:
        swim_speed = (self.length_pool
                      * self.count_pool
                      / self.M_IN_KM
                      / self.duration)
        return swim_speed

    def get_spent_calories(self) -> float:
        swimming_calories = ((self.get_mean_speed()
                             + self.COEF_CALORIE_5)
                             * self.COEF_CALORIE_6
                             * self.weight)
        return swimming_calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict_training = {'SWM': Swimming,
                     'RUN': Running,
                     'WLK': SportsWalking}
    if workout_type not in dict_training:
        raise ValueError('Такой тренировки нет.')
    return dict_training[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
