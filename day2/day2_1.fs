module Day2020_21

    open FS
    open System.Text.RegularExpressions

    type PasswordAndPolicy = {RequiredCharacter:char; MinOccurence:int; MaxOccurence:int;Password:string}
    type PasswordValidity = {PasswordAndPolicy:PasswordAndPolicy; IsValid:bool}

    let (|Regex|_|) pattern input =
        let m = Regex.Match(input, pattern)
        if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
        else None


    let validatePassword passwordAndPolicy =
        let password = passwordAndPolicy.Password
        let countOfRequiredChar = password
                                  |> Seq.toList
                                  |> List.filter (fun charValue -> charValue = passwordAndPolicy.RequiredCharacter)
                                  |> List.length
        let isPasswordValid = countOfRequiredChar >= passwordAndPolicy.MinOccurence && countOfRequiredChar <= passwordAndPolicy.MaxOccurence

        {PasswordAndPolicy=passwordAndPolicy; IsValid = isPasswordValid}



    let validatePasswords passwordAndPolicyList =
        passwordAndPolicyList
        |> List.map validatePassword

    let convertLinesToPasswordAndPolicy line =
        match line with
        | Regex @"([0-9]+)-([0-9]+) ([a-z]+)\: (.*)$" [ min; max; requiredCharacter; password ] ->
            {MinOccurence=(int min); MaxOccurence=(int max); RequiredCharacter=(char requiredCharacter); Password=(string password)}
        | _ -> failwith "invalid input"

    let buildPasswordAndPolicyList lines =
        lines |> List.map convertLinesToPasswordAndPolicy

    let countValidPasswords passwordLines =
        passwordLines |> buildPasswordAndPolicyList
        |> validatePasswords
        |> List.filter (fun passwordValidity -> passwordValidity.IsValid)
        |> List.length
    let executeTest =
        //let expenses = readfile "Day1" |> Array.map (fun value -> value |> int) |> Array.toList
        let passwordLines = [
            "1-3 a: abcde";
            "1-3 b: cdefg";
            "2-9 c: ccccccccc"
        ]

        passwordLines |> countValidPasswords
        //|> countValidity

    let execute =
        let passwordLines = readfile "Day2" |> Array.toList

        passwordLines |> countValidPasswords