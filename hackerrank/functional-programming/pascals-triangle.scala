// https://www.hackerrank.com/challenges/pascals-triangle

object Solution {

  def pascalTriangle(k: Int): Unit = {
    var row = List(1)
    println(row.mkString(" "))
    for (i <- 2 to k) {
      row = (0 :: row) zip (row ++ List(0)) map (p => p._1 + p._2)
      println(row.mkString(" "))
    }
  }

  def main(args: Array[String]): Unit = {
    val lines = io.Source.stdin.getLines()
    pascalTriangle(lines.next.toInt)
  }
}
