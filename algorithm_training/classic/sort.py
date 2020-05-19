#
# Author: George Lei

import random
import math

def bubble_sort(arr):
  n = len(arr)
  for i in range(n - 1):
    for j in range(i + 1, n):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr

def insert_sort(arr):
  for i in range(len(arr)):
    cur = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > cur:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = cur
  return arr

def merge_sort(arr, low=0, hi=-1):
  if hi == -1:
    hi = len(arr)

  if hi - low == 1:
    return arr[low:hi]
  
  mid = (hi + low) // 2
  arr1 = merge_sort(arr, low, mid)
  arr2 = merge_sort(arr, mid, hi)

  result, i, j = [], 0, 0
  while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
      result.append(arr1[i])
      i += 1
    else:
      result.append(arr2[j])
      j += 1

  while i < len(arr1):
    result.append(arr1[i])
    i += 1
  while j < len(arr2):
    result.append(arr2[j])
    j += 1

  return result


def quick_sort(arr, low=0, hi=-1):
  if hi == -1:
    hi = len(arr)

  index = qs_partition(arr, low, hi)
  if index - low > 1:
    quick_sort(arr, low, index)
  if hi - index > 2:
    quick_sort(arr, index + 1, hi)

  return arr

def qs_partition(arr, low, hi):
  pivot = arr[hi-1]
  i = low - 1
  for j in range(low, hi):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  return i

def heap_sort(arr):
  n = len(arr)
  for i in range(n // 2, -1, -1):
    heapify_max(arr, n, i)

  for i in range(n - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify_max(arr, i, 0)

  return arr

def heapify_max(arr, n, cur):
  left, right = cur * 2 + 1, cur * 2 + 2

  largest = cur
  if left < n and arr[left] > arr[largest]:
    largest = left
  if right < n and arr[right] > arr[largest]:
    largest = right

  if cur != largest:
    arr[cur], arr[largest] = arr[largest], arr[cur]
    heapify_max(arr, n, largest)


def radix_sort(arr):
  max_num = max(arr)
  n = int(math.log10(max_num))

  for i in range(n + 1):
    func = lambda x: x % 10 ** (i + 1) // 10 ** i
    arr = counting_sort(arr, func)

  return arr


def counting_sort(arr, func):
  buckets = [[] for i in range(10)]

  for num in arr:
    buckets[func(num)].append(num)

  result = []
  for bucket in buckets:
    result.extend(bucket)

  return result

algorithms = [('Bubble Sort', bubble_sort), ('Insert Sort', insert_sort),
              ('Merge Sort', merge_sort), ('Quick Sort', quick_sort),
              ('Heap Sort', heap_sort), ('Radix Sort', radix_sort)]

test_cases = [
  {
    'name': '10 numbers',
    'in': [[0, 8, 2, 6, 9, 7, 3, 1, 4, 5]],
    'out': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  },
  {
    'name': '100 numbers',
    'in': [[57, 20, 86, 7, 90, 87, 64, 44, 85, 66, 75, 0, 98, 99, 6, 40, 28, 4, 2, 38, 11, 41, 96, 95, 14, 62, 56, 59, 79, 69, 71, 21, 91, 92, 60, 80, 25, 23, 83, 67, 61, 8, 18, 29, 34, 15, 94, 30, 55, 97, 54, 13, 31, 42, 9, 63, 12, 17, 76, 3, 46, 37, 35, 33, 32, 48, 51, 43, 78, 93, 49, 10, 52, 74, 70, 50, 19, 81, 65, 26, 1, 53, 58, 84, 73, 82, 24, 45, 22, 5, 77, 72, 89, 68, 88, 16, 39, 47, 36, 27]],
    'out': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
  },
  {
    'name': '1000 numbers',
    'in': [[599, 221, 372, 764, 633, 568, 687, 231, 758, 546, 120, 737, 719, 960, 447, 548, 51, 744, 713, 939, 681, 795, 331, 556, 70, 58, 955, 350, 998, 977, 205, 449, 535, 198, 657, 158, 626, 772, 213, 990, 312, 330, 222, 542, 321, 811, 13, 791, 543, 729, 255, 319, 440, 392, 216, 293, 407, 656, 593, 328, 379, 135, 699, 999, 985, 11, 554, 489, 303, 580, 595, 338, 817, 156, 885, 89, 290, 857, 425, 505, 436, 382, 170, 484, 103, 908, 211, 80, 251, 130, 954, 734, 292, 139, 183, 921, 868, 769, 665, 2, 855, 206, 650, 95, 193, 504, 258, 105, 677, 968, 833, 652, 503, 726, 300, 899, 241, 553, 877, 209, 423, 203, 561, 230, 801, 279, 41, 919, 508, 256, 247, 108, 60, 953, 443, 337, 943, 662, 664, 485, 753, 967, 644, 906, 174, 273, 907, 55, 886, 257, 909, 784, 136, 86, 409, 591, 782, 500, 840, 217, 812, 701, 668, 910, 229, 155, 854, 663, 494, 620, 889, 427, 858, 678, 281, 87, 234, 525, 531, 849, 536, 592, 612, 90, 283, 264, 357, 961, 104, 917, 286, 604, 276, 199, 950, 196, 435, 570, 311, 963, 695, 523, 515, 747, 989, 765, 743, 682, 53, 555, 28, 454, 841, 125, 498, 396, 517, 29, 469, 645, 475, 806, 167, 14, 853, 417, 62, 361, 308, 182, 479, 9, 430, 172, 957, 924, 157, 715, 934, 326, 894, 453, 740, 288, 709, 363, 422, 189, 684, 177, 16, 814, 374, 25, 225, 895, 918, 162, 647, 755, 659, 550, 71, 527, 77, 47, 470, 274, 506, 81, 519, 437, 341, 54, 238, 166, 923, 163, 204, 798, 82, 141, 869, 803, 78, 951, 349, 91, 683, 85, 688, 344, 819, 916, 459, 161, 571, 322, 267, 839, 224, 996, 164, 215, 815, 110, 113, 848, 173, 295, 966, 403, 466, 509, 616, 3, 354, 660, 649, 577, 946, 752, 733, 383, 797, 674, 280, 723, 304, 501, 450, 426, 972, 455, 748, 958, 832, 846, 228, 970, 575, 965, 477, 171, 346, 790, 866, 107, 76, 534, 578, 676, 638, 463, 739, 859, 825, 212, 249, 394, 920, 551, 714, 835, 116, 391, 807, 617, 202, 123, 298, 37, 262, 640, 220, 903, 192, 184, 400, 666, 880, 583, 359, 147, 323, 913, 799, 654, 947, 873, 398, 181, 533, 66, 395, 75, 945, 26, 253, 891, 342, 244, 452, 727, 21, 530, 165, 223, 842, 826, 900, 424, 268, 314, 756, 607, 925, 487, 68, 34, 1, 867, 478, 686, 763, 529, 928, 492, 152, 99, 40, 387, 981, 731, 987, 847, 693, 931, 545, 783, 277, 902, 52, 464, 901, 879, 474, 904, 637, 896, 702, 827, 316, 250, 456, 788, 679, 808, 486, 898, 451, 594, 7, 810, 252, 285, 818, 759, 188, 511, 863, 914, 512, 112, 393, 340, 779, 415, 862, 829, 347, 138, 745, 565, 722, 830, 823, 547, 358, 94, 911, 619, 585, 672, 219, 995, 334, 838, 750, 348, 49, 121, 959, 370, 299, 667, 773, 411, 777, 540, 412, 458, 785, 227, 476, 598, 353, 457, 149, 609, 878, 446, 614, 915, 201, 969, 888, 516, 355, 153, 707, 694, 775, 499, 890, 5, 860, 628, 635, 431, 208, 186, 416, 572, 272, 828, 294, 302, 325, 22, 291, 776, 518, 414, 439, 589, 942, 126, 386, 245, 19, 805, 569, 929, 462, 8, 655, 941, 480, 521, 610, 404, 460, 207, 320, 563, 442, 708, 587, 643, 127, 705, 711, 581, 365, 73, 380, 882, 933, 134, 39, 259, 345, 564, 926, 962, 472, 413, 124, 586, 938, 952, 735, 30, 675, 749, 579, 143, 948, 10, 17, 122, 520, 718, 653, 210, 680, 691, 780, 912, 385, 717, 639, 64, 725, 993, 119, 133, 601, 544, 140, 836, 700, 613, 176, 65, 724, 481, 115, 864, 816, 720, 448, 507, 490, 983, 43, 786, 488, 761, 106, 623, 287, 871, 621, 482, 622, 742, 865, 159, 974, 420, 824, 937, 971, 306, 692, 92, 697, 557, 324, 997, 493, 532, 590, 502, 844, 438, 301, 956, 696, 317, 513, 377, 467, 497, 197, 887, 634, 522, 399, 432, 175, 566, 964, 876, 905, 870, 200, 781, 433, 624, 872, 88, 444, 754, 150, 584, 364, 102, 703, 148, 539, 704, 336, 698, 892, 6, 15, 191, 940, 738, 874, 235, 284, 36, 982, 63, 560, 327, 732, 48, 369, 352, 309, 240, 770, 465, 496, 160, 766, 596, 582, 935, 18, 275, 767, 434, 145, 339, 72, 794, 128, 552, 685, 574, 74, 428, 137, 932, 236, 843, 605, 109, 180, 243, 602, 567, 98, 893, 271, 514, 721, 246, 310, 278, 631, 976, 774, 93, 646, 771, 289, 625, 69, 24, 741, 146, 214, 856, 296, 922, 388, 389, 730, 831, 630, 537, 261, 789, 991, 232, 343, 802, 526, 538, 850, 461, 429, 883, 603, 397, 661, 332, 483, 402, 820, 50, 768, 129, 762, 986, 588, 851, 491, 706, 541, 651, 975, 673, 307, 670, 59, 716, 822, 237, 778, 930, 45, 333, 845, 67, 576, 973, 131, 441, 636, 187, 710, 178, 736, 746, 760, 270, 378, 629, 405, 32, 804, 495, 632, 558, 524, 642, 728, 384, 390, 101, 861, 615, 978, 168, 194, 689, 360, 600, 23, 38, 35, 473, 944, 185, 169, 27, 111, 408, 142, 936, 226, 994, 46, 269, 375, 787, 33, 445, 712, 132, 79, 793, 233, 356, 821, 0, 313, 266, 573, 884, 751, 792, 373, 83, 690, 980, 608, 179, 381, 949, 611, 421, 31, 559, 658, 242, 671, 118, 367, 282, 151, 852, 897, 117, 606, 57, 195, 875, 471, 318, 114, 351, 96, 260, 648, 549, 992, 154, 627, 468, 406, 401, 988, 837, 297, 335, 61, 528, 4, 20, 305, 669, 881, 984, 597, 329, 366, 263, 376, 371, 927, 42, 190, 44, 418, 979, 100, 796, 419, 315, 368, 254, 800, 218, 834, 12, 809, 562, 248, 265, 510, 813, 618, 641, 410, 362, 84, 239, 97, 144, 56, 757]],
    'out': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999]
  }]

def generate_random_test_cases():
  test_cases = []
  for _ in range(10):
    size = random.randint(200, 5000)
    output = [i for i in range(size)]
    input = list(output)
    for i in range(size - 1):
      j = random.randint(i, size - 1)
      input[i], input[j] = input[j], input[i]

    test_cases.append({
      'name': 'Random {} numbers'.format(size),
      'in': [input],
      'out': output
    })
  return test_cases

test_cases += generate_random_test_cases()