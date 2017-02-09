// https://www.hackerrank.com/challenges/pairs

import collection.mutable

object Solution {
  def main(args: Array[String]): Unit = {
    val firstLineValues = io.StdIn.readLine().split(" ")
    val (n, k) = (firstLineValues(0).toInt, firstLineValues(1).toInt)
    val numbers = io.StdIn.readLine().split(" ").map(_.toInt).toList
    assert(numbers.size == n)
    assert(numbers.forall(_ > 0))

    val z = (0, mutable.Map.empty[Int, Int].withDefaultValue(0))
    val result = numbers.foldLeft(z) { (accumul, elem) =>
      val (oldCount, mem) = accumul
      val newCount = oldCount + mem(elem)
      mem(elem + k) += 1
      if (elem - k > 0) mem(elem - k) += 1
      (newCount, mem)
    }._1

    println(result)
  }
}