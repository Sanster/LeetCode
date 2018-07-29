class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        count = 0
        while z != 0:
            if z % 2 == 1:
                count += 1
            z = z // 2

        return count

    def hammingDistance2(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


if __name__ == "__main__":
    s = Solution()
    assert s.hammingDistance(1, 4) == 2
    assert s.hammingDistance(1, 1) == 0
    assert s.hammingDistance(4, 4) == 0
    assert s.hammingDistance(8, 4) == 2

    assert s.hammingDistance2(1, 4) == 2
    assert s.hammingDistance2(1, 1) == 0
    assert s.hammingDistance2(4, 4) == 0
    assert s.hammingDistance2(8, 4) == 2
