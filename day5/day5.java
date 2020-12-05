import java.util.List;

public class Day5 {

    public int decodeSeat(String code) {
        return decodeRow(code) * 8 + decodeColumn(code);
    }

    public int decodeRow(String code) {
        return decode(code.substring(0, 7), "F", "B");
    }

    public int decodeColumn(String code) {
        return decode(code.substring(7), "L", "R");
    }

    private int decode(String code, String lowKey, String highKey) {
        var binaryRepresentation =
                code.replaceAll(lowKey, "0")
                    .replaceAll(highKey, "1");
        return Integer.parseInt(binaryRepresentation, 2);
    }

    public int highestSeatId(List<String> seatCodes) {
        return seatCodes.stream()
                .mapToInt(this::decodeSeat)
                .max()
                .orElse(0);
    }

    public int missingSeatId(List<String> seatCodes) {
        var stats = seatCodes.stream()
                .mapToInt(this::decodeSeat)
                .summaryStatistics();
        int max = stats.getMax();
        int min = stats.getMin();
        var sumOfConsecutiveIntFromMinToMax = max * (max + 1) / 2 - (min - 1) * min / 2;
        return sumOfConsecutiveIntFromMinToMax - (int) stats.getSum();
    }

}
