// https://www.hackerrank.com/challenges/string-compression

object Solution {

  def compress(s: String, c: Char, n: Int, sout: StringBuilder): String = {
    if (s.length == 0 || s.head != c) {
      val cout = n match {
        case 0 => ""
        case 1 => c.toString
        case _ => s"$c$n"
      }
      sout ++= cout
      s.length match {
        case 0 => sout.toString
        case _ => compress(s.tail, s.head, 1, sout)
      }
    } else {
      compress(s.tail, c, n + 1, sout)
    }
  }

  def main(args: Array[String]): Unit = {
    val lines = io.Source.stdin.getLines()
    val msg = lines.next()
    println(compress(msg, '\u0000', 0, new StringBuilder))
  }
}
