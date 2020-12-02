fun main() {
    val s = getInputLines(2020, 1).map { it.toInt() }.sorted()

    println(s.filter { a -> a <= 2020 / 2 }
        .flatMapIndexed { ai, a -> s.filterIndexed { bi, b -> bi > ai && a + b == 2020 }.map { b -> a * b } }.first())

    println(s.filter { a -> a <= 2020 / 3 }
        .flatMapIndexed { ai, a ->
            s.filterIndexed { bi, b -> bi > ai && b <= 2020 / 2 }.flatMapIndexed { bi, b ->
                s.filterIndexed { ci, c -> ci > bi && a + b + c == 2020 }.map { c -> a * b * c }
            }
        }.first())
}
