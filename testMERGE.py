#!/usr/bin/python3

import MERGE

import unittest



class TestMergeMethod(unittest.TestCase):

    def test_empty_list(self):
        no_tupel = []
        self.assertEqual(MERGE.merge(no_tupel), no_tupel, "Passing empty List of tupels.")

    def test_only_one_tupel(self):
        inout=[[25,30]]
        self.assertEqual(MERGE.merge(inout), inout, "Passing only one tupel.")

    def test_same_tupel(self):
        in_tupel = [[25,30],[25,30]]
        out_tupel = [[25,30]]
        self.assertEqual(MERGE.merge(in_tupel), out_tupel, "Passing a tupel twice.")

    def test_no_merge(self):
        in_tupel = [[1,3],[4,6]]
        out_tupel = [[1,3],[4,6]]
        self.assertEqual(MERGE.merge(in_tupel), out_tupel, "No Merge.")

    def test_the_bigger_ones(self):
        in_tupel = [[1,3],[4,6], [5,7] ]
        out_tupel = [[1,3],[4,7]]
        self.assertEqual(MERGE.merge(in_tupel), out_tupel, "Merge the two bigger ones out of three.")

    def test_int_and_float_mixing(self):
        in_tupel = [[1,3] ,[0.4,1.8]]
        out_tupel = [[0.4, 3.0]]
        self.assertEqual(MERGE.merge(in_tupel), out_tupel, "Passing mixed int and floats.")

    def test_three_overlapping_intervalls(self):
        in_tupel = [[1,3], [2,4], [3,5]]
        out_tupel = [[1 , 5]]
        self.assertEqual(MERGE.merge(in_tupel), out_tupel, "Passing three overlapping intervalls.")

    def test_on_around_another(self):
        in_tupel = [[1,9], [2, 8]]
        out_tupel = [[1 , 9]]
        self.assertEqual(MERGE.merge(in_tupel), out_tupel, "Passing one wrapping the other.")

if __name__ == '__main__':
    unittest.main()
