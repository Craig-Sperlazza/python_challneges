from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    item_list = []
    if len(nums1) <= len(nums2):
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                item_list.append(nums1[i])
                nums2.remove(nums1[i])
    else:
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                item_list.append(nums2[j])
                nums1.remove(nums2[j])
    return item_list

    



if __name__ == "__main__":
    x = [1,2,2,1]
    y = [2,2]
    print(intersect(x,y))

    a = [4,9,5]
    z = [9,4,9,8,4]
    print(intersect(a,z))

    lc1 = [3,1,2]
    lc2 = [1,1]
    print(intersect(lc1,lc2))
