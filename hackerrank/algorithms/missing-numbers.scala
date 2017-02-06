// https://www.hackerrank.com/challenges/missing-numbers

object Solution {

  def main(args: Array[String]): Unit = {
    val n = io.StdIn.readInt()
    val firstList = readListFromStdIn()
    assert(n == firstList.size)

    val m = io.StdIn.readInt()
    val secondList = readListFromStdIn()
    assert(m  == secondList.size)

    val result = findMissingNumbers(firstList, secondList)
    println(result.map(_.toString).mkString(" "))
  }

  def readListFromStdIn(): Seq[Int] = io.StdIn.readLine().split(" ").map(_.toInt)

  def findMissingNumbers(firstList: Seq[Int], secondList: Seq[Int]): Seq[Int] = {
    val firstListCounts = countNumbers(firstList)
    val secondListCounts = countNumbers(secondList)
    secondListCounts.flatMap { case (k, secondListCount) =>
        val firstListCount = firstListCounts.getOrElse(k, 0)
        if (secondListCount > firstListCount) Seq(k) else Seq()
    }.toSeq.sorted
  }

  def countNumbers(list: Seq[Int]): Map[Int, Int] = list.groupBy(identity).mapValues(_.size).toMap
}