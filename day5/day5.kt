package fr.lidonis.adventofcode.y2020.day5
class BinaryBoardingScanner(scan: List<String>) {
    private val sortedPassIds = scan.map {
        it.replace(Regex("[BR]"), "1")
            .replace(Regex("[FL]"), "0")
            .toInt(2)
    }.sorted()
    fun highestSeatID() = sortedPassIds.last()
    fun findMissingSeatId() = (sortedPassIds.zipWithNext().first { it.first + 1 != it.second }).first + 1
}