import java.util.*;

public class Day3 {

    public Day3(List<String> map) {
        this.map = map;
        this.patternLength = map.get(0).length();
        this.patternHeight = map.size();
    }

    public Geology onPosition(int xPosition, int yPosition) {
        return Geology.ofPosition(map.get(yPosition).charAt(xPosition % patternLength));
    }

    public int treesOnRope(int right, int down) {
        int treesFound = 0;
        for (int x = right, y = down; y < patternHeight; x += right, y += down) {
            if (Geology.TREE == onPosition(x, y)) {
                treesFound++;
            }
        }
        return treesFound;
    }

    enum Geology {
        OPEN_SQUARE, TREE;

        static Geology ofPosition(char representation) {
            return representation == '.' ? OPEN_SQUARE : TREE;
        }
    }

    private final List<String> map;
    private final int patternLength;
    private final int patternHeight;
}
