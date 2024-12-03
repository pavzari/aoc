from itertools import pairwise


def _is_report_safe(report: list) -> bool:
    if 0 in report:
        return False
    elif max(report) > 3 or min(report) < -3:
        return False
    elif not all(
        [
            abs(pair[0]) + abs(pair[1]) == abs(pair[0] + pair[1])
            for pair in pairwise(report)
        ]
    ):
        return False
    return True


def _try_ignore_level(levels: list) -> bool:
    for i in range(len(levels)):
        removed_level = levels[:i] + levels[i + 1 :]
        new_level_changes = [pair[0] - pair[1] for pair in pairwise(removed_level)]
        if _is_report_safe(new_level_changes):
            return True
    return False


def part_one(level_changes: list[list]) -> int:
    return [_is_report_safe(report) for report in level_changes].count(True)


def part_two(input, level_changes) -> int:
    safe_reports = []
    for index, report in enumerate(level_changes):
        if not _is_report_safe(report):
            safe_reports.append(_try_ignore_level(input[index]))
        else:
            safe_reports.append(True)
    return safe_reports.count(True)


if __name__ == "__main__":
    input = [line.strip() for line in open("input/d2", "r").readlines()]
    input = [list(map(int, report.split(" "))) for report in input]

    level_changes = [
        [pair[0] - pair[1] for pair in pairwise(report)] for report in input
    ]
    print(part_one(level_changes))
    print(part_two(input, level_changes))
