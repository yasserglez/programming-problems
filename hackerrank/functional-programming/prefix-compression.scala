object Solution {

  def prefixCompression(x: String, y: String, p: String = ""): List[String] = {
    if (x.isEmpty || y.isEmpty || x.head != y.head) {
      List(p, x, y)
    } else {
      prefixCompression(x.tail, y.tail, p + x.head)
    }
  }

  def main(args: Array[String]): Unit = {
    val lines = io.Source.stdin.getLines()
    val result = prefixCompression(lines.next(), lines.next())
    result foreach (s => println(s"${s.length} $s"))
  }
}
