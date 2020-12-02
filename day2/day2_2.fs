module Day2020_22

    open FS
    open System.Text.RegularExpressions

    type PasswordAndOfficialTobogganCorporateAuthenticationSystemPolicy = {RequiredCharacter:char; Position1:int; Position2:int;Password:string}
    type PasswordValidity = {PasswordAndPolicy:PasswordAndOfficialTobogganCorporateAuthenticationSystemPolicy; IsValid:bool}

    let (|Regex|_|) pattern input =
        let m = Regex.Match(input, pattern)
        if m.Success then Some(List.tail [ for g in m.Groups -> g.Value ])
        else None

    let validatePassword passwordAndPolicy =
        let passwordChars = passwordAndPolicy.Password |> Seq.toArray
        let charInPolicyPosition1 = passwordChars.[passwordAndPolicy.Position1-1]
        let charInPolicyPosition2 = passwordChars.[passwordAndPolicy.Position2-1]
        let isRequiredCharInPosition1 = charInPolicyPosition1 = passwordAndPolicy.RequiredCharacter
        let isRequiredCharInPosition2 = charInPolicyPosition2 = passwordAndPolicy.RequiredCharacter
        let isPasswordValid = (isRequiredCharInPosition1 && not isRequiredCharInPosition2)
                              || (not isRequiredCharInPosition1 && isRequiredCharInPosition2)


        {PasswordAndPolicy=passwordAndPolicy; IsValid = isPasswordValid}


    let validatePasswords passwordAndPolicyList =
        passwordAndPolicyList
        |> List.map validatePassword

    let convertLinesToPasswordAndPolicy line =
        match line with
        | Regex @"([0-9]+)-([0-9]+) ([a-z]+)\: (.*)$" [ min; max; requiredCharacter; password ] ->
            {Position1=(int min); Position2=(int max); RequiredCharacter=(char requiredCharacter); Password=(string password)}
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