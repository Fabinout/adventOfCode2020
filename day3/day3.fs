module Day2020_32

    open FS
    type Square = Tree|OpenSquare
    type SpacedTreeLines = Square array
    type Area = {SpacedTreeLines: SpacedTreeLines array}

    let buildSquare (cell:char) =
        match cell with
        | '#' -> Tree
        | '.' -> OpenSquare
        | _ -> failwith "invalid cell value"
    let buildSpacedTreeLine (line:string) =
        line |> Seq.toList
        |> List.map buildSquare
        |> List.toArray
    let buildArea (input:string[]) =
        let spacedTreeLines = input |> Array.map (fun line -> buildSpacedTreeLine line)
        {SpacedTreeLines=spacedTreeLines}

    let rec slide right down startingFrom hitTrees area =
        let (startingFromRow, startingFromColumn) = startingFrom
        let (landingRow, landingColumn) = (startingFromRow+down, startingFromColumn+right)
        printfn "row : %i, col: %i" landingRow landingColumn
        let patternLength = area.SpacedTreeLines.[0].Length
        let (targetRowInAreaPattern, targetColumnInAreaPattern) = (landingRow, landingColumn % patternLength)
        printfn "targetRowInArea : %i, targetColumnInArea: %i" targetRowInAreaPattern targetColumnInAreaPattern

        match targetRowInAreaPattern with
        | y when y >= area.SpacedTreeLines.Length ->
            printfn "pattern %i-%i : %i trees" right down hitTrees
            hitTrees
        | _ ->
            match area.SpacedTreeLines.[targetRowInAreaPattern].[targetColumnInAreaPattern] with
            | Tree -> slide right down (targetRowInAreaPattern,targetColumnInAreaPattern) (hitTrees+1) area
            | OpenSquare -> slide right down (targetRowInAreaPattern,targetColumnInAreaPattern) hitTrees area


    let productOfHitTreesForAllSlidePatterns area =
        let slidePatterns = [|(1, 1);(3, 1);(5, 1);(7, 1);(1, 2)|]
        slidePatterns
        |> Array.map (fun (right, down) -> slide right down (0,0) 0 area)
        |> Array.reduce (fun acc treeCount -> acc * treeCount)
    let executeTest =
        let puzzleInput =
            "..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"

        let area = puzzleInput.Split "\n" |> buildArea
        productOfHitTreesForAllSlidePatterns area

    let execute =
        let puzzleInput = readfile "Day3"
        let area = puzzleInput |> buildArea

        productOfHitTreesForAllSlidePatterns area