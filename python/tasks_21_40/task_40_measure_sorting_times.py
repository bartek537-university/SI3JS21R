import statistics
from datetime import timedelta, datetime
from io import TextIOWrapper
from typing import Final, Callable

from python.tasks_21_40.sorting_algorithms import bubble_sort, insertion_sort, quick_sort


def load_numbers_from_file(file_name: str) -> list[float]:
    with open(file_name) as file:
        return [float(line) for line in file]


UNSORTED_NUMBERS_FILE_NAMES: Final[list[str]] = [
    "nieposortowane_a.txt",
    "nieposortowane_b.txt",
    "nieposortowane_c.txt",
    "nieposortowane_d.txt",
]

unsorted_numbers: list[list[float]] = []

for unsorted_numbers_file_name in UNSORTED_NUMBERS_FILE_NAMES:
    unsorted_numbers.append(load_numbers_from_file(unsorted_numbers_file_name))


class BenchmarkResult:
    def __init__(self, algorithm_name: str, measurements: list[timedelta]):
        self.algorithm_name = algorithm_name
        self.measurements_seconds = BenchmarkResult._convert_measurements_to_seconds(measurements)

    @staticmethod
    def _convert_measurements_to_seconds(measurements: list[timedelta]) -> list[float]:
        return [measurement.total_seconds() for measurement in measurements]

    def __len__(self):
        return len(self.measurements_seconds)

    def get_mean_time_seconds(self) -> float:
        return statistics.mean(self.measurements_seconds)

    def get_standard_deviation_seconds(self) -> float:
        return statistics.stdev(self.measurements_seconds)


def write_file_line(file_writer: TextIOWrapper, values: list[...], delimiter: str = " ") -> None:
    file_writer.write(f"{delimiter.join(map(str, values))}\n")


COLUMN_DELIMITER: Final[str] = " -- "


def file_write_benchmark_results(file_writer: TextIOWrapper, results: list[BenchmarkResult]) -> None:
    write_file_line(file_writer, [
        "NAZWA",
        "LICZBA SORTOWANYCH PLIKÓW",
        "ŚREDNI CZAS",
        "ODCHYLENIE STANDARDOWE"
    ], COLUMN_DELIMITER)

    for index, result in enumerate(results):
        write_file_line(file_writer, [
            f"{index + 1}. {result.algorithm_name}",
            len(result),
            f"{result.get_mean_time_seconds():f} s",
            f"{result.get_standard_deviation_seconds():f} s",
        ], COLUMN_DELIMITER)


Algorithm = tuple[str, Callable[[list[...]], None]]

ALGORITHMS: Final[list[Algorithm]] = [
    ("bąbelkowe", lambda numbers: bubble_sort(numbers)),
    ("przez wstawienie", lambda numbers: insertion_sort(numbers)),
    ("szybkie", lambda numbers: quick_sort(numbers, 0, len(numbers))),
]

benchmark_results: list[BenchmarkResult] = []


def measure_time(fn: Callable[[], None]) -> timedelta:
    start_time = datetime.now()
    fn()
    end_time = datetime.now()
    return end_time - start_time


for name, algorithm in ALGORITHMS:
    measured_times = [measure_time(lambda: algorithm(numbers)) for numbers in unsorted_numbers]
    benchmark_results.append(BenchmarkResult(name, measured_times))

FULL_DATETIME_FORMAT: Final[str] = "%Y%m%d%H%M%S"


def get_report_file_name(timestamp: datetime) -> str:
    formatted_timestamp = timestamp.strftime(FULL_DATETIME_FORMAT)
    return f"raport_{formatted_timestamp}.txt"


report_file_name = get_report_file_name(datetime.now())
with open(report_file_name, "w+") as report_file:
    report_file.write("RAPORT ALGORYTMÓW SORTOWANIA\n")
    file_write_benchmark_results(report_file, benchmark_results)
