// https://www.hackerrank.com/challenges/remove-duplicates

object Solution {
  def removeDuplicates(str: String): String = {
    str.length match {
      case 0 => ""
      case _ => str.head + removeDuplicates(str.tail.filter(_ != str.head))
    }
  }

  def main(args: Array[String]): Unit = {
    val str = io.Source.stdin.getLines().next
    println(removeDuplicates(str))
  }
}
