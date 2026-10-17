"""Tests for the Advent of Code 2017 solutions.

Two kinds of tests are included:

* ``TestExamples`` checks each solution against the official examples from
  the puzzle descriptions. These run anywhere.
* ``TestFullInputs`` runs each ``main`` against the real puzzle input and
  compares the output to the known correct answers. These are skipped when
  the (private, uncommitted) input file is not present.
"""
import importlib
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DAYS = list(range(1, 26))

# Correct answers for the real puzzle inputs, keyed by day.
EXPECTED_ANSWERS = {
    1: ("1393", "1292"),
    2: ("45351", "275"),
    3: ("480", "349975"),
    4: ("466", "251"),
    5: ("372139", "29629538"),
    6: ("11137", "1037"),
    7: ("hlqnsbe", "1993"),
    8: ("4416", "5199"),
    9: ("7616", "3838"),
    10: ("9656", "20b7b54c92bf73cf3e5631458a715149"),
    11: ("743", "1493"),
    12: ("130", "189"),
    13: ("1476", "3937334"),
    14: ("8216", "1139"),
    15: ("577", "316"),
    16: ("dcmlhejnifpokgba", "ifocbejpdnklamhg"),
    17: ("1670", "2316253"),
    18: ("3423", "7493"),
    19: ("GSXDIPWTU", "16100"),
    20: ("157", "499"),
    21: ("123", "1984683"),
    22: ("5176", "2512017"),
    23: ("3969", "917"),
    24: ("1940", "1928"),
    25: ("4230",),
}


def input_path(day):
    return ROOT / f"day{day:02d}" / f"day{day:02d}.txt"


def load_module(day):
    return importlib.import_module(f"day{day:02d}.day{day:02d}")


def run_main(day):
    module = load_module(day)
    output = io.StringIO()
    with redirect_stdout(output):
        module.main()
    return output.getvalue()


class TestImports(unittest.TestCase):
    def test_every_day_imports_and_exposes_main(self):
        for day in DAYS:
            with self.subTest(day=day):
                module = load_module(day)
                self.assertTrue(callable(getattr(module, "main", None)))


class TestExamples(unittest.TestCase):
    def test_day01(self):
        from day01.day01 import find_captcha_solution, find_captcha_solution_part_two

        self.assertEqual(
            [find_captcha_solution(x) for x in ("1122", "1111", "1234", "91212129")],
            [3, 4, 0, 9],
        )
        self.assertEqual(
            [
                find_captcha_solution_part_two(x)
                for x in ("1212", "1221", "123425", "123123", "12131415")
            ],
            [6, 0, 4, 12, 4],
        )

    def test_day02(self):
        from day02.day02 import (
            calculate_spreadsheet_checksum,
            calculate_spreadsheet_checksum_part_two,
        )

        self.assertEqual(
            calculate_spreadsheet_checksum("5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8"), 18
        )
        self.assertEqual(
            calculate_spreadsheet_checksum_part_two("5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5"),
            9,
        )

    def test_day03(self):
        from day03.day03 import find_manhattan_distance_to_access_point

        self.assertEqual(
            [
                find_manhattan_distance_to_access_point(str(n))
                for n in (12, 23, 1024)
            ],
            [3, 2, 31],
        )

    def test_day04(self):
        from day04.day04 import (
            find_valid_passphrases,
            find_valid_passphrases_with_extra_security,
        )

        self.assertEqual(
            find_valid_passphrases("aa bb cc dd ee\naa bb cc dd aa\naa bb cc dd aaa"), 2
        )
        self.assertEqual(
            find_valid_passphrases_with_extra_security(
                "abcde fghij\n"
                "abcde xyz ecdab\n"
                "a ab abc abd abf abj\n"
                "iiii oiii ooii oooi oooo\n"
                "oiii ioii iioi iiio"
            ),
            3,
        )

    def test_day05(self):
        from day05.day05 import (
            find_number_of_steps_to_reach_exit,
            find_number_of_steps_to_reach_exit_part_two,
        )

        self.assertEqual(find_number_of_steps_to_reach_exit("0\n3\n0\n1\n-3"), 5)
        self.assertEqual(
            find_number_of_steps_to_reach_exit_part_two("0\n3\n0\n1\n-3"), 10
        )

    def test_day06(self):
        from day06.day06 import (
            find_cycle_length,
            find_number_of_cycles_before_duplicate,
        )

        self.assertEqual(find_number_of_cycles_before_duplicate("0\t2\t7\t0"), 5)
        self.assertEqual(find_cycle_length("0\t2\t7\t0"), 4)

    def test_day07(self):
        from day07.day07 import find_balancing_weight, find_name_of_bottom_program

        data = (
            "pbga (66)\n"
            "xhth (57)\n"
            "ebii (61)\n"
            "havc (66)\n"
            "ktlj (57)\n"
            "fwft (72) -> ktlj, cntj, xhth\n"
            "qoyq (66)\n"
            "padx (45) -> pbga, havc, qoyq\n"
            "tknk (41) -> ugml, padx, fwft\n"
            "jptl (61)\n"
            "ugml (68) -> gyxo, ebii, jptl\n"
            "gyxo (61)\n"
            "cntj (57)"
        )
        self.assertEqual(find_name_of_bottom_program(data), "tknk")
        self.assertEqual(find_balancing_weight(data), 60)

    def test_day08(self):
        from day08.day08 import (
            find_largest_value_during_process,
            find_largest_value_in_register,
        )

        data = (
            "b inc 5 if a > 1\n"
            "a inc 1 if b < 5\n"
            "c dec -10 if a >= 1\n"
            "c inc -20 if c == 10"
        )
        self.assertEqual(find_largest_value_in_register(data), 1)
        self.assertEqual(find_largest_value_during_process(data), 10)

    def test_day09(self):
        from day09.day09 import (
            calculate_total_score,
            find_non_canceled_characters_within_garbage,
        )

        self.assertEqual(
            [calculate_total_score(x) for x in ("{}", "{{{}}}", "{{},{}}", "{{{},{},{{}}}}")],
            [1, 6, 5, 16],
        )
        self.assertEqual(
            find_non_canceled_characters_within_garbage("{<a>,<a>,<a>,<a>}"), 4
        )

    def test_day10(self):
        from day10.day10 import find_knot_hash

        self.assertEqual(find_knot_hash(""), "a2582a3a0e66e6e86e3812dcb672a272")
        self.assertEqual(find_knot_hash("AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")
        self.assertEqual(find_knot_hash("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")
        self.assertEqual(find_knot_hash("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")

    def test_day11(self):
        from day11.day11 import calculate_steps

        self.assertEqual(
            [
                calculate_steps(x)
                for x in ("ne,ne,ne", "ne,ne,sw,sw", "ne,ne,s,s", "se,sw,se,sw,sw")
            ],
            [3, 0, 2, 3],
        )

    def test_day12(self):
        from day12.day12 import (
            find_number_of_groups,
            find_number_of_programs_connected_to_zero,
        )

        data = (
            "0 <-> 2\n"
            "1 <-> 1\n"
            "2 <-> 0, 3, 4\n"
            "3 <-> 2, 4\n"
            "4 <-> 2, 3, 6\n"
            "5 <-> 6\n"
            "6 <-> 4, 5"
        )
        self.assertEqual(find_number_of_programs_connected_to_zero(data), 6)
        self.assertEqual(find_number_of_groups(data), 2)

    def test_day13(self):
        from day13.day13 import (
            calculate_severity,
            calculate_smallest_delay_remain_undetected,
        )

        data = "0: 3\n1: 2\n4: 4\n6: 4"
        self.assertEqual(calculate_severity(data), 24)
        self.assertEqual(calculate_smallest_delay_remain_undetected(data), 10)

    def test_day14(self):
        from day14.day14 import (
            calculate_number_of_present_regions,
            calculate_number_of_used_squares,
        )

        self.assertEqual(calculate_number_of_used_squares("flqrgnkx"), 8108)
        self.assertEqual(calculate_number_of_present_regions("flqrgnkx"), 1242)

    def test_day15(self):
        import day15.day15 as day15

        generator = getattr(day15, "__generator")
        count_matching = getattr(day15, "__count_matching_pairs")

        def first_values(seed, factor, multiple=1):
            sequence = generator(seed, factor, multiple)
            return [next(sequence) for _ in range(5)]

        # First five generated values from the official example.
        self.assertEqual(
            first_values(65, day15.GENERATOR_A_FACTOR),
            [1092455, 1181022009, 245556042, 1744312007, 1352636452],
        )
        self.assertEqual(
            first_values(8921, day15.GENERATOR_B_FACTOR),
            [430625591, 1233683848, 1431495498, 137874439, 285222916],
        )
        # First five values accepted under part 2's criteria.
        self.assertEqual(
            first_values(65, day15.GENERATOR_A_FACTOR, 4),
            [1352636452, 1992081072, 530830436, 1980017072, 740335192],
        )
        self.assertEqual(
            first_values(8921, day15.GENERATOR_B_FACTOR, 8),
            [1233683848, 862516352, 1159784568, 1616057672, 412269392],
        )

        # The example's third pair is the first to match, giving 1 after
        # five pairs. (The full 40M/5M runs are covered by TestFullInputs.)
        data = "Generator A starts with 65\nGenerator B starts with 8921"
        self.assertEqual(count_matching(data, 2), 0)
        self.assertEqual(count_matching(data, 3), 1)
        self.assertEqual(count_matching(data, 5), 1)

    def test_day16(self):
        from day16.day16 import find_program_order

        self.assertEqual(find_program_order("s1"), "pabcdefghijklmno")
        self.assertEqual(find_program_order("x0/15"), "pbcdefghijklmnoa")
        self.assertEqual(find_program_order("pa/p"), "pbcdefghijklmnoa")
        self.assertEqual(find_program_order("s3,x0/15,pa/b"), "mopbacdefghijkln")

    def test_day17(self):
        from day17.day17 import find_value_after_2017

        self.assertEqual(find_value_after_2017(3), 638)

    def test_day18(self):
        from day18.day18 import find_value_of_recovered_frequency

        # The official example uses literal operands (``snd 1``), which this
        # register-based implementation does not support, so use an equivalent
        # register-only program.
        self.assertEqual(find_value_of_recovered_frequency("set a 1\nsnd a\nrcv a"), 1)
        self.assertEqual(
            find_value_of_recovered_frequency("set a 1\nsnd a\nset a 0\nrcv a"), 0
        )

    def test_day19(self):
        from day19.day19 import calculate_number_of_steps, find_route

        data = (
            "     |          \n"
            "     |  +--+    \n"
            "     A  |  C    \n"
            " F---|----E|--+ \n"
            "     |  |  |  D \n"
            "     +B-+  +--+ "
        )
        self.assertEqual(find_route(data), ("ABCDEF", 38))
        self.assertEqual(calculate_number_of_steps(data), 38)

    def test_day20(self):
        from day20.day20 import (
            find_number_of_particles_left,
            find_particle_closest_to_origin_for_longest,
        )

        part_one = (
            "p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>\n"
            "p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>"
        )
        part_two = (
            "p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>\n"
            "p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>\n"
            "p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>\n"
            "p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>"
        )
        self.assertEqual(find_particle_closest_to_origin_for_longest(part_one), 0)
        self.assertEqual(find_number_of_particles_left(part_two), 1)

    def test_day21(self):
        # The public functions are pinned to 5/18 iterations, whereas the
        # official example documents its result after 2 iterations, so test
        # the parameterised helper directly. getattr avoids name mangling.
        import day21.day21 as day21

        solve = getattr(day21, "__number_of_pixels_on_after_n_iterations")
        data = "../.# => ##./#../...\n.#./..#/### => #..#/..../..../#..#"
        self.assertEqual(solve(data, 2), 12)

    def test_day22(self):
        from day22.day22 import find_number_of_bursts_that_infect_a_node

        self.assertEqual(
            find_number_of_bursts_that_infect_a_node("..#\n#..\n..."), 5587
        )

    def test_day23(self):
        from day23.day23 import (
            _is_prime,
            find_number_of_times_mul_is_invoked,
            find_value_left_in_register_h,
        )

        self.assertTrue(all(_is_prime(n) for n in (2, 3, 5, 7, 11, 97)))
        self.assertFalse(any(_is_prime(n) for n in (0, 1, 4, 6, 9, 100)))
        self.assertEqual(find_number_of_times_mul_is_invoked("set a 5\nmul a a"), 1)
        self.assertEqual(find_value_left_in_register_h(), 917)

    def test_day24(self):
        from day24.day24 import (
            find_strength_of_the_longest_bridge,
            find_strongest_bridge,
        )

        data = "0/2\n2/2\n2/3\n3/4\n3/5\n0/1\n10/1\n9/10"
        self.assertEqual(find_strongest_bridge(data), 31)
        self.assertEqual(find_strength_of_the_longest_bridge(data), 19)

    def test_day25(self):
        from day25.day25 import find_diagnostic_checksum

        self.assertEqual(find_diagnostic_checksum(), 4230)


class TestFullInputs(unittest.TestCase):
    def test_answers_match_expected(self):
        for day, expected in EXPECTED_ANSWERS.items():
            path = input_path(day)
            if not path.exists():
                continue
            with self.subTest(day=day):
                output = run_main(day)
                actual = tuple(
                    line.split(": ", 1)[1]
                    for line in output.splitlines()
                    if line.startswith("Part ")
                )
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
