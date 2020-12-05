module Day2020_42

    open FS
    open StringHelper


    type ValidatedBYR = ValidatedBYR of int

    let validateBYR value =
        match value with
        | Int i when i >= 1920 && i <= 2002 -> Some (ValidatedBYR i)
        | _ ->
                printfn "value not matching byr %s" value
                None

    type ValidatedIYR = ValidatedIYR of int

    let validateIYR value =
        match value with
        | Int i when i >= 2010 && i <= 2020 -> Some (ValidatedIYR i)
        | _ -> None

    type ValidatedEYR = ValidatedEYR of int

    let validateEYR value =
        match value with
        | Int i when i >= 2020 && i <= 2030 -> Some (ValidatedEYR i)
        | _ -> None

    type HeightUnit = CM | IN

    let validateHeightUnit unit =
        match unit with
        | "cm" -> Some CM
        | "in" -> Some IN
        | _ -> None

    type ValidatedHGT = int * HeightUnit

    let validateHGT value =
        match value with
        | Regex @"([0-9]{2,3})([a-z]{2})$" [ height; unit ] ->
            let validatedUnit = validateHeightUnit unit
            match validatedUnit with
            | Some CM -> if (int height) >= 150 && (int height) <= 193 then Some (ValidatedHGT (int height, validatedUnit.Value)) else None
            | Some IN -> if (int height) >= 59 && (int height) <= 76 then Some (ValidatedHGT (int height, validatedUnit.Value)) else None
            | None -> None
        | _ -> None


    type ValidatedHCL = ValidatedHCL of string
    let validateHCL value =
        match value with
        | Regex @"^(#[0-9|a-f]{6})$" [ color ] ->
            Some (ValidatedHCL color)
        | _ -> None

    type ValidatedECL = AMB | BLU | BRN | GRY | GRN | HZL | OTH
    let validateECL value =
        match value with
        | "amb" -> Some AMB
        | "blu" -> Some BLU
        | "brn" -> Some BRN
        | "gry" -> Some GRY
        | "grn" -> Some GRN
        | "hzl" -> Some HZL
        | "oth" -> Some OTH
        | _ -> None

    type ValidatedPID = ValidatedPID of string
    let validatePID value =
        match value with
        | Regex @"^([0-9]{9})$" [ id ] ->
            Some (ValidatedPID id)
        | _ -> None

    type ValidatedCID = ValidatedCID of string
    let validateCID value = Some (ValidatedCID value)

    type Passport = {
        Byr:ValidatedBYR option
        Iyr:ValidatedIYR option
        Eyr:ValidatedEYR option
        Hgt:ValidatedHGT option
        Hcl:ValidatedHCL option
        Ecl:ValidatedECL option
        Pid:ValidatedPID option
        Cid:ValidatedCID option
    }

    let addAndValidateField passport (fieldNameAndValue:string) =
        let fieldAndValue = fieldNameAndValue.Split ":"
        let field = (fieldAndValue.[0], fieldAndValue.[1])
        match field with
        | ("byr", value) -> {passport with Byr=validateBYR value}
        | ("iyr", value) -> {passport with Iyr=validateIYR value}
        | ("eyr", value) -> {passport with Eyr=validateEYR value}
        | ("hgt", value) -> {passport with Hgt=validateHGT value}
        | ("hcl", value) -> {passport with Hcl=validateHCL value}
        | ("ecl", value) -> {passport with Ecl=validateECL value}
        | ("pid", value) -> {passport with Pid=validatePID value}
        | ("cid", value) -> {passport with Cid=validateCID value}
        | _ -> failwith "invalid passport structure"

    let buildPassport (passportFields:string) =
        let fieldNameAndValues = passportFields.Split " "
        let passport = {Byr=None;Iyr=None;Eyr=None;Hgt=None;Hcl=None;Ecl=None;Pid=None;Cid=None}
        let result = fieldNameAndValues |> Seq.fold addAndValidateField passport
        printfn "PASSPORT : %A" result
        result

    let buildPassportList (passportList: string seq) =
        passportList |> Seq.map (buildPassport) //[[|"a:b;c:d"|];[|"a:b;c:d"|]

    let isValid password =
        password.Byr.IsSome &&
        password.Iyr.IsSome &&
        password.Eyr.IsSome &&
        password.Hgt.IsSome &&
        password.Hcl.IsSome &&
        password.Ecl.IsSome &&
        password.Pid.IsSome

    let countValidPassports passports =

        passports |> Seq.filter (fun passport -> passport |> isValid)
        |> Seq.length

    let solve (puzzleInput:string) =
        puzzleInput.Split "\n\n"
        |> Array.toSeq
        |> Seq.map (replace "\n" " ")
        |> buildPassportList
        |> countValidPassports
    let executeTest =
        let validPuzzleInput1 =
            "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
        solve validPuzzleInput1

    let execute =
        readfileAsString "Day4" |> solve