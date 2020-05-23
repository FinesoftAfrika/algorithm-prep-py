# https://github.com/georgezlei/algorithm-training-py
# Author: George Lei

import random
import bisect

def list_index(arr, target):
  '''For benchmark purpose only'''
  try:
    return arr.index(target)
  except ValueError:
    return -1

def python_bisect(arr, target):
  index = bisect.bisect_left(arr, target)
  if arr[index] == target:
    return index
  return -1

def bisearch(arr, target):
  '''Binary search for non-duplicate increasing arrays'''
  low, hi = 0, len(arr) - 1

  while low <= hi:
    mid = (low + hi) // 2
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      low = mid + 1
    else:
      hi = mid - 1

  return -1

algorithms = [
  ('Python list index', list_index),
  ('Python bisect', python_bisect),
  ('Binary search', bisearch)
]

test_cases = [
  {
    'name': '100 numbers',
    'in': [[1, 24, 66, 104, 145, 157, 173, 195, 230, 273, 278, 302, 305, 341, 367, 368, 409, 439, 467, 515, 531, 556, 565, 573, 579, 594, 629, 665, 679, 704, 725, 764, 766, 795, 820, 834, 858, 865, 892, 923, 958, 961, 970, 975, 1017, 1036, 1062, 1102, 1111, 1156, 1177, 1208, 1252, 1258, 1289, 1311, 1344, 1367, 1383, 1405, 1452, 1479, 1519, 1565, 1571, 1578, 1623, 1645, 1649, 1664, 1695, 1745, 1768, 1790, 1836, 1837, 1839, 1874, 1916, 1947, 1953, 1957, 1991, 2016, 2039, 2053, 2100, 2117, 2155, 2186, 2194, 2207, 2244, 2278, 2319, 2335, 2343, 2353, 2357, 2369], 2343],
    'out': 96
  },
  {
    'name': '100 numbers not found',
    'in': [[1, 24, 66, 104, 145, 157, 173, 195, 230, 273, 278, 302, 305, 341, 367, 368, 409, 439, 467, 515, 531, 556, 565, 573, 579, 594, 629, 665, 679, 704, 725, 764, 766, 795, 820, 834, 858, 865, 892, 923, 958, 961, 970, 975, 1017, 1036, 1062, 1102, 1111, 1156, 1177, 1208, 1252, 1258, 1289, 1311, 1344, 1367, 1383, 1405, 1452, 1479, 1519, 1565, 1571, 1578, 1623, 1645, 1649, 1664, 1695, 1745, 1768, 1790, 1836, 1837, 1839, 1874, 1916, 1947, 1953, 1957, 1991, 2016, 2039, 2053, 2100, 2117, 2155, 2186, 2194, 2207, 2244, 2278, 2319, 2335, 2343, 2353, 2357, 2369], 2344],
    'out': -1
  },
  {
    'name': '1000 numbers',
    'in': [[1, 4, 14, 28, 65, 78, 92, 129, 174, 213, 243, 261, 304, 321, 360, 405, 434, 474, 524, 555, 572, 615, 635, 641, 666, 716, 720, 747, 768, 810, 833, 834, 846, 860, 879, 880, 917, 936, 959, 1007, 1038, 1070, 1074, 1109, 1156, 1170, 1220, 1233, 1248, 1279, 1294, 1303, 1341, 1381, 1422, 1472, 1499, 1500, 1508, 1550, 1592, 1619, 1660, 1665, 1695, 1733, 1749, 1769, 1790, 1840, 1890, 1933, 1955, 1965, 1996, 2007, 2014, 2048, 2074, 2102, 2119, 2161, 2204, 2215, 2255, 2284, 2312, 2316, 2320, 2350, 2372, 2379, 2394, 2405, 2406, 2424, 2460, 2462, 2480, 2505, 2538, 2562, 2590, 2622, 2661, 2689, 2698, 2741, 2750, 2755, 2804, 2852, 2877, 2915, 2950, 2967, 3014, 3032, 3048, 3081, 3090, 3137, 3170, 3200, 3247, 3258, 3301, 3345, 3384, 3386, 3390, 3412, 3443, 3456, 3467, 3497, 3538, 3551, 3591, 3626, 3630, 3644, 3688, 3689, 3737, 3780, 3811, 3850, 3868, 3882, 3893, 3932, 3964, 3978, 3990, 4020, 4037, 4054, 4096, 4099, 4145, 4161, 4192, 4237, 4268, 4301, 4337, 4362, 4407, 4456, 4475, 4480, 4523, 4545, 4586, 4625, 4669, 4698, 4729, 4749, 4790, 4833, 4843, 4884, 4898, 4935, 4969, 4970, 5005, 5054, 5084, 5107, 5119, 5149, 5197, 5230, 5261, 5308, 5345, 5384, 5421, 5426, 5458, 5464, 5503, 5538, 5564, 5599, 5636, 5685, 5726, 5754, 5803, 5847, 5850, 5873, 5913, 5933, 5939, 5972, 5995, 6002, 6024, 6032, 6058, 6063, 6113, 6158, 6189, 6225, 6251, 6278, 6323, 6372, 6393, 6427, 6476, 6480, 6526, 6567, 6617, 6629, 6674, 6692, 6703, 6745, 6758, 6797, 6809, 6833, 6867, 6876, 6910, 6958, 6988, 7010, 7058, 7081, 7087, 7115, 7143, 7160, 7200, 7236, 7258, 7265, 7311, 7322, 7342, 7365, 7415, 7422, 7447, 7459, 7490, 7507, 7539, 7568, 7609, 7612, 7642, 7646, 7671, 7679, 7681, 7700, 7704, 7706, 7718, 7748, 7769, 7800, 7833, 7844, 7861, 7889, 7935, 7957, 7985, 7999, 8033, 8051, 8074, 8101, 8125, 8150, 8191, 8206, 8230, 8245, 8252, 8279, 8291, 8340, 8360, 8377, 8388, 8390, 8432, 8460, 8494, 8532, 8551, 8576, 8590, 8610, 8636, 8664, 8714, 8762, 8796, 8810, 8836, 8868, 8890, 8916, 8960, 9002, 9048, 9071, 9114, 9157, 9177, 9224, 9267, 9284, 9313, 9362, 9405, 9424, 9471, 9496, 9516, 9538, 9588, 9621, 9669, 9685, 9722, 9739, 9769, 9812, 9858, 9901, 9946, 9975, 9979, 10011, 10022, 10062, 10106, 10148, 10167, 10215, 10218, 10264, 10267, 10309, 10347, 10390, 10418, 10448, 10498, 10511, 10553, 10589, 10624, 10629, 10648, 10670, 10717, 10733, 10772, 10817, 10844, 10868, 10918, 10946, 10965, 10976, 10990, 11001, 11047, 11059, 11098, 11100, 11116, 11130, 11166, 11201, 11246, 11251, 11257, 11297, 11343, 11383, 11413, 11430, 11472, 11473, 11475, 11486, 11526, 11574, 11618, 11635, 11646, 11662, 11685, 11699, 11741, 11787, 11825, 11841, 11855, 11865, 11901, 11904, 11918, 11962, 12007, 12029, 12044, 12065, 12115, 12128, 12166, 12170, 12209, 12244, 12278, 12311, 12312, 12343, 12372, 12379, 12383, 12424, 12463, 12465, 12508, 12509, 12526, 12527, 12576, 12609, 12655, 12688, 12723, 12741, 12763, 12764, 12804, 12817, 12819, 12856, 12901, 12947, 12989, 13004, 13021, 13063, 13067, 13073, 13081, 13120, 13145, 13178, 13184, 13211, 13222, 13247, 13261, 13271, 13319, 13336, 13339, 13376, 13395, 13417, 13429, 13474, 13502, 13532, 13551, 13561, 13597, 13642, 13676, 13701, 13731, 13755, 13774, 13817, 13854, 13885, 13906, 13936, 13978, 13982, 14005, 14051, 14069, 14071, 14103, 14150, 14181, 14227, 14266, 14295, 14307, 14319, 14337, 14362, 14406, 14413, 14461, 14465, 14479, 14524, 14528, 14548, 14553, 14595, 14596, 14609, 14619, 14641, 14665, 14666, 14693, 14743, 14783, 14827, 14867, 14889, 14935, 14971, 14977, 15004, 15051, 15085, 15091, 15133, 15148, 15167, 15204, 15230, 15250, 15275, 15312, 15346, 15393, 15398, 15419, 15456, 15457, 15470, 15487, 15499, 15542, 15560, 15589, 15592, 15600, 15605, 15631, 15635, 15649, 15697, 15708, 15715, 15760, 15787, 15788, 15803, 15816, 15817, 15854, 15863, 15900, 15935, 15964, 16005, 16047, 16068, 16093, 16143, 16163, 16210, 16253, 16279, 16321, 16349, 16372, 16414, 16423, 16453, 16499, 16523, 16547, 16560, 16603, 16644, 16691, 16709, 16750, 16770, 16773, 16787, 16826, 16865, 16881, 16897, 16899, 16929, 16979, 17005, 17017, 17052, 17100, 17101, 17110, 17149, 17168, 17183, 17221, 17222, 17234, 17264, 17305, 17345, 17382, 17432, 17479, 17510, 17544, 17570, 17615, 17621, 17626, 17646, 17678, 17726, 17750, 17760, 17768, 17811, 17842, 17850, 17861, 17889, 17931, 17966, 17992, 18018, 18063, 18076, 18111, 18141, 18191, 18219, 18253, 18289, 18336, 18342, 18383, 18422, 18454, 18492, 18520, 18570, 18615, 18638, 18646, 18658, 18703, 18714, 18728, 18768, 18777, 18814, 18836, 18881, 18899, 18949, 18959, 18994, 19003, 19040, 19048, 19079, 19088, 19089, 19130, 19179, 19228, 19238, 19263, 19297, 19341, 19368, 19418, 19462, 19493, 19531, 19573, 19620, 19656, 19687, 19705, 19735, 19782, 19798, 19832, 19881, 19911, 19919, 19928, 19968, 19969, 19993, 20041, 20077, 20102, 20150, 20195, 20212, 20244, 20294, 20343, 20358, 20379, 20397, 20399, 20430, 20467, 20483, 20501, 20510, 20551, 20563, 20592, 20631, 20666, 20695, 20729, 20732, 20756, 20801, 20844, 20846, 20856, 20867, 20884, 20894, 20938, 20947, 20979, 20994, 21031, 21037, 21038, 21087, 21094, 21124, 21173, 21198, 21211, 21221, 21235, 21266, 21294, 21320, 21368, 21392, 21414, 21441, 21442, 21457, 21477, 21519, 21565, 21596, 21638, 21672, 21705, 21723, 21726, 21764, 21789, 21794, 21809, 21837, 21880, 21927, 21953, 21987, 22031, 22052, 22058, 22106, 22115, 22148, 22155, 22204, 22210, 22239, 22265, 22275, 22308, 22357, 22402, 22413, 22427, 22435, 22474, 22491, 22505, 22552, 22594, 22641, 22664, 22712, 22725, 22739, 22767, 22816, 22865, 22868, 22912, 22923, 22966, 23011, 23032, 23060, 23079, 23112, 23152, 23182, 23224, 23245, 23295, 23301, 23317, 23352, 23366, 23406, 23423, 23425, 23426, 23439, 23476, 23485, 23522, 23555, 23556, 23557, 23588, 23591, 23626, 23649, 23667, 23695, 23709, 23721, 23723, 23765, 23789, 23808, 23846, 23856, 23905, 23952, 23994, 24013, 24025, 24069, 24110, 24127, 24147, 24192, 24213, 24219, 24240, 24243, 24256, 24274, 24294, 24339, 24346, 24348, 24392, 24422, 24444, 24463, 24488, 24517, 24519, 24535, 24536, 24586, 24613, 24660, 24667, 24674, 24699, 24718, 24762, 24779, 24787, 24791, 24819, 24834, 24840, 24873, 24916, 24937, 24986, 25019, 25039, 25085, 25129, 25130, 25178, 25198, 25205, 25254, 25282, 25293, 25311, 25330, 25359, 25398, 25441, 25473, 25502, 25518, 25563, 25609, 25651, 25696, 25698, 25705, 25746, 25754, 25775, 25777, 25803, 25833, 25859, 25876, 25887, 25894, 25941, 25943, 25992, 26001, 26028, 26055, 26066, 26098, 26140, 26160, 26170, 26218, 26234, 26263, 26312, 26323, 26371, 26373, 26380, 26410, 26438, 26484, 26516, 26551, 26581, 26588], 26581],
    'out': 998
  },
  {
    'name': '1000 numbers not found',
    'in': [[1, 4, 14, 28, 65, 78, 92, 129, 174, 213, 243, 261, 304, 321, 360, 405, 434, 474, 524, 555, 572, 615, 635, 641, 666, 716, 720, 747, 768, 810, 833, 834, 846, 860, 879, 880, 917, 936, 959, 1007, 1038, 1070, 1074, 1109, 1156, 1170, 1220, 1233, 1248, 1279, 1294, 1303, 1341, 1381, 1422, 1472, 1499, 1500, 1508, 1550, 1592, 1619, 1660, 1665, 1695, 1733, 1749, 1769, 1790, 1840, 1890, 1933, 1955, 1965, 1996, 2007, 2014, 2048, 2074, 2102, 2119, 2161, 2204, 2215, 2255, 2284, 2312, 2316, 2320, 2350, 2372, 2379, 2394, 2405, 2406, 2424, 2460, 2462, 2480, 2505, 2538, 2562, 2590, 2622, 2661, 2689, 2698, 2741, 2750, 2755, 2804, 2852, 2877, 2915, 2950, 2967, 3014, 3032, 3048, 3081, 3090, 3137, 3170, 3200, 3247, 3258, 3301, 3345, 3384, 3386, 3390, 3412, 3443, 3456, 3467, 3497, 3538, 3551, 3591, 3626, 3630, 3644, 3688, 3689, 3737, 3780, 3811, 3850, 3868, 3882, 3893, 3932, 3964, 3978, 3990, 4020, 4037, 4054, 4096, 4099, 4145, 4161, 4192, 4237, 4268, 4301, 4337, 4362, 4407, 4456, 4475, 4480, 4523, 4545, 4586, 4625, 4669, 4698, 4729, 4749, 4790, 4833, 4843, 4884, 4898, 4935, 4969, 4970, 5005, 5054, 5084, 5107, 5119, 5149, 5197, 5230, 5261, 5308, 5345, 5384, 5421, 5426, 5458, 5464, 5503, 5538, 5564, 5599, 5636, 5685, 5726, 5754, 5803, 5847, 5850, 5873, 5913, 5933, 5939, 5972, 5995, 6002, 6024, 6032, 6058, 6063, 6113, 6158, 6189, 6225, 6251, 6278, 6323, 6372, 6393, 6427, 6476, 6480, 6526, 6567, 6617, 6629, 6674, 6692, 6703, 6745, 6758, 6797, 6809, 6833, 6867, 6876, 6910, 6958, 6988, 7010, 7058, 7081, 7087, 7115, 7143, 7160, 7200, 7236, 7258, 7265, 7311, 7322, 7342, 7365, 7415, 7422, 7447, 7459, 7490, 7507, 7539, 7568, 7609, 7612, 7642, 7646, 7671, 7679, 7681, 7700, 7704, 7706, 7718, 7748, 7769, 7800, 7833, 7844, 7861, 7889, 7935, 7957, 7985, 7999, 8033, 8051, 8074, 8101, 8125, 8150, 8191, 8206, 8230, 8245, 8252, 8279, 8291, 8340, 8360, 8377, 8388, 8390, 8432, 8460, 8494, 8532, 8551, 8576, 8590, 8610, 8636, 8664, 8714, 8762, 8796, 8810, 8836, 8868, 8890, 8916, 8960, 9002, 9048, 9071, 9114, 9157, 9177, 9224, 9267, 9284, 9313, 9362, 9405, 9424, 9471, 9496, 9516, 9538, 9588, 9621, 9669, 9685, 9722, 9739, 9769, 9812, 9858, 9901, 9946, 9975, 9979, 10011, 10022, 10062, 10106, 10148, 10167, 10215, 10218, 10264, 10267, 10309, 10347, 10390, 10418, 10448, 10498, 10511, 10553, 10589, 10624, 10629, 10648, 10670, 10717, 10733, 10772, 10817, 10844, 10868, 10918, 10946, 10965, 10976, 10990, 11001, 11047, 11059, 11098, 11100, 11116, 11130, 11166, 11201, 11246, 11251, 11257, 11297, 11343, 11383, 11413, 11430, 11472, 11473, 11475, 11486, 11526, 11574, 11618, 11635, 11646, 11662, 11685, 11699, 11741, 11787, 11825, 11841, 11855, 11865, 11901, 11904, 11918, 11962, 12007, 12029, 12044, 12065, 12115, 12128, 12166, 12170, 12209, 12244, 12278, 12311, 12312, 12343, 12372, 12379, 12383, 12424, 12463, 12465, 12508, 12509, 12526, 12527, 12576, 12609, 12655, 12688, 12723, 12741, 12763, 12764, 12804, 12817, 12819, 12856, 12901, 12947, 12989, 13004, 13021, 13063, 13067, 13073, 13081, 13120, 13145, 13178, 13184, 13211, 13222, 13247, 13261, 13271, 13319, 13336, 13339, 13376, 13395, 13417, 13429, 13474, 13502, 13532, 13551, 13561, 13597, 13642, 13676, 13701, 13731, 13755, 13774, 13817, 13854, 13885, 13906, 13936, 13978, 13982, 14005, 14051, 14069, 14071, 14103, 14150, 14181, 14227, 14266, 14295, 14307, 14319, 14337, 14362, 14406, 14413, 14461, 14465, 14479, 14524, 14528, 14548, 14553, 14595, 14596, 14609, 14619, 14641, 14665, 14666, 14693, 14743, 14783, 14827, 14867, 14889, 14935, 14971, 14977, 15004, 15051, 15085, 15091, 15133, 15148, 15167, 15204, 15230, 15250, 15275, 15312, 15346, 15393, 15398, 15419, 15456, 15457, 15470, 15487, 15499, 15542, 15560, 15589, 15592, 15600, 15605, 15631, 15635, 15649, 15697, 15708, 15715, 15760, 15787, 15788, 15803, 15816, 15817, 15854, 15863, 15900, 15935, 15964, 16005, 16047, 16068, 16093, 16143, 16163, 16210, 16253, 16279, 16321, 16349, 16372, 16414, 16423, 16453, 16499, 16523, 16547, 16560, 16603, 16644, 16691, 16709, 16750, 16770, 16773, 16787, 16826, 16865, 16881, 16897, 16899, 16929, 16979, 17005, 17017, 17052, 17100, 17101, 17110, 17149, 17168, 17183, 17221, 17222, 17234, 17264, 17305, 17345, 17382, 17432, 17479, 17510, 17544, 17570, 17615, 17621, 17626, 17646, 17678, 17726, 17750, 17760, 17768, 17811, 17842, 17850, 17861, 17889, 17931, 17966, 17992, 18018, 18063, 18076, 18111, 18141, 18191, 18219, 18253, 18289, 18336, 18342, 18383, 18422, 18454, 18492, 18520, 18570, 18615, 18638, 18646, 18658, 18703, 18714, 18728, 18768, 18777, 18814, 18836, 18881, 18899, 18949, 18959, 18994, 19003, 19040, 19048, 19079, 19088, 19089, 19130, 19179, 19228, 19238, 19263, 19297, 19341, 19368, 19418, 19462, 19493, 19531, 19573, 19620, 19656, 19687, 19705, 19735, 19782, 19798, 19832, 19881, 19911, 19919, 19928, 19968, 19969, 19993, 20041, 20077, 20102, 20150, 20195, 20212, 20244, 20294, 20343, 20358, 20379, 20397, 20399, 20430, 20467, 20483, 20501, 20510, 20551, 20563, 20592, 20631, 20666, 20695, 20729, 20732, 20756, 20801, 20844, 20846, 20856, 20867, 20884, 20894, 20938, 20947, 20979, 20994, 21031, 21037, 21038, 21087, 21094, 21124, 21173, 21198, 21211, 21221, 21235, 21266, 21294, 21320, 21368, 21392, 21414, 21441, 21442, 21457, 21477, 21519, 21565, 21596, 21638, 21672, 21705, 21723, 21726, 21764, 21789, 21794, 21809, 21837, 21880, 21927, 21953, 21987, 22031, 22052, 22058, 22106, 22115, 22148, 22155, 22204, 22210, 22239, 22265, 22275, 22308, 22357, 22402, 22413, 22427, 22435, 22474, 22491, 22505, 22552, 22594, 22641, 22664, 22712, 22725, 22739, 22767, 22816, 22865, 22868, 22912, 22923, 22966, 23011, 23032, 23060, 23079, 23112, 23152, 23182, 23224, 23245, 23295, 23301, 23317, 23352, 23366, 23406, 23423, 23425, 23426, 23439, 23476, 23485, 23522, 23555, 23556, 23557, 23588, 23591, 23626, 23649, 23667, 23695, 23709, 23721, 23723, 23765, 23789, 23808, 23846, 23856, 23905, 23952, 23994, 24013, 24025, 24069, 24110, 24127, 24147, 24192, 24213, 24219, 24240, 24243, 24256, 24274, 24294, 24339, 24346, 24348, 24392, 24422, 24444, 24463, 24488, 24517, 24519, 24535, 24536, 24586, 24613, 24660, 24667, 24674, 24699, 24718, 24762, 24779, 24787, 24791, 24819, 24834, 24840, 24873, 24916, 24937, 24986, 25019, 25039, 25085, 25129, 25130, 25178, 25198, 25205, 25254, 25282, 25293, 25311, 25330, 25359, 25398, 25441, 25473, 25502, 25518, 25563, 25609, 25651, 25696, 25698, 25705, 25746, 25754, 25775, 25777, 25803, 25833, 25859, 25876, 25887, 25894, 25941, 25943, 25992, 26001, 26028, 26055, 26066, 26098, 26140, 26160, 26170, 26218, 26234, 26263, 26312, 26323, 26371, 26373, 26380, 26410, 26438, 26484, 26516, 26551, 26581, 26588], 26582],
    'out': -1
  },
]

def generate_non_duplicate_test_cases():
  ''' Generate 10 random test cases.'''
  test_cases = []
  for _ in range(10):
    size = random.randint(100000, 500000)

    arr = [0] * size
    i = 1
    while i < size:
      arr[i] = arr[i-1] + random.randint(1, 50)
      i += 1

    index = random.randint(0, size - 1)
    target = arr[index]

    test_cases.append({
      'name': 'Random {} numbers'.format(len(arr)),
      'in': [arr, target],
      'out': index
    })
  return test_cases

test_cases += generate_non_duplicate_test_cases()