module Day2020_82

    open FS
    open StringHelper
    
    type Operation = JMP | NOP | ACC
    type Instruction = {Operation:Operation; Value:int}
    type Result = Success | Failure
        
    let buildInstruction instruction =
        match instruction with
        | Regex @"acc (.*)" [ value ] ->
            {Operation=ACC; Value=(int value)}; 
        | Regex @"jmp (.*)" [ value ] ->
            {Operation=JMP; Value=(int value)}
        | Regex @"nop (.*)$" [ value ] ->
            {Operation=NOP; Value=0}
        | i ->
            printfn "invalid instruction %A" i
            failwith "invalid instruction"

    
    
    let buildProgram (code:string) =
        let program = code.Split "\n"
        program |> Array.map buildInstruction
        
    let rec executeAndStopOnInfiniteLoopOrSuccessOrInvalidProgram position accumulator (runPositions:int array) (program:Instruction array) =
        if position = program.Length then (accumulator, Success)
        else if runPositions |> Array.contains position then (accumulator, Failure)
        else if position <0 then (accumulator, Failure)
        else 
            let instruction = program.[position]
            
            match instruction with
            | {Operation=ACC; Value=value} ->
                let newPosition = position + 1
                let newAccumulator = accumulator + value
                let newRunPositions = Array.append runPositions [|position|]
                executeAndStopOnInfiniteLoopOrSuccessOrInvalidProgram newPosition newAccumulator newRunPositions program
            | {Operation=JMP; Value=value} ->
                let newPosition = position + value
                let newRunPositions = Array.append runPositions [|position|]
                executeAndStopOnInfiniteLoopOrSuccessOrInvalidProgram newPosition accumulator newRunPositions program 
            | {Operation=NOP; Value=value} ->
                let newPosition = position + 1
                let newRunPositions = Array.append runPositions [|position|]
                executeAndStopOnInfiniteLoopOrSuccessOrInvalidProgram newPosition accumulator newRunPositions program             
   
      
    let buildVariation (program:Instruction array) position fromOperation toOperation =
        let (newProgram:Instruction array) = Array.copy program
        newProgram.[position] <- {program.[position] with Operation=toOperation}
        newProgram
   
    
    let solve input = 
        let originalProgram = input |> buildProgram
        let mutable programVariations = [||]
        for i in 0..originalProgram.Length-1 do
            if originalProgram.[i].Operation = JMP
            then
                programVariations <- programVariations |> Array.append [|(buildVariation originalProgram i JMP NOP)|]
            else if originalProgram.[i].Operation = NOP
            then
                programVariations <- programVariations |> Array.append [|(buildVariation originalProgram i NOP JMP)|]
            else
                programVariations <- programVariations
        
        let winnerProgram = programVariations
                            |> Array.tryFind (fun program ->
                                let (accumulator, result) = program |> executeAndStopOnInfiniteLoopOrSuccessOrInvalidProgram 0 0 [||]
                                if result = Success then true else false
                                )
        if winnerProgram.IsNone
        then 0
        else 
            let (accumulator, status) = executeAndStopOnInfiniteLoopOrSuccessOrInvalidProgram 0 0 [||] winnerProgram.Value
            accumulator
         
         
    let executeTest =
        let input = "nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"
        let dumbInput = "nop +0"
        solve input
    
    let execute =
        let input = readfileAsString "Day8"
        solve input
        
