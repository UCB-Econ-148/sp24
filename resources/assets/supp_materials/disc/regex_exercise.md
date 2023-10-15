---
layout: default
title: Regex Exercises
nav_exclude: true
description: Regex exercise
---


# Regex Exercises

## Exercise 1
**Find words that start with “ex” for the following:**

```
exactly	
radiation
table
explosive
exposed
decade
ministry
excluding
expected
suffering
excitement
Story
```

[Regex101 Link](https://regex101.com/r/nqlvgd/1)



## Exercise 2
**Find the SIDs for the following:** 

```
Name: Oski, Year: ???, SID: 123456789
Name: Leon, Year: Senior, SID: 382049283 (this is just something random)
Name: Peter, Year: Junior, SID: 329840020 (also something random)
```

[Regex101 Link](https://regex101.com/r/55sVFw/1)


## Exercise 3 
**Find the API keys for the following:** 

```
Leon’s API key: uy3829hoipufhp9w8aanoi (don’t use)
Peter’s API key: 489qp3nfshfSsphf09HWan 
Eric’s API key: DEMO_KEY he used this in lecture!
```

[Regex101 Link](https://regex101.com/r/A5xzEE/1)


## Exercise 4
**Find the years in the following table:**

```
| Year | value |
| - - - | - - - |
| 1956 | 135436132 |
| 2001 | 86435233 |
| 2008 | 1368543 |
| 2077 | 168463213 |
```

[Regex101 Link](https://regex101.com/r/V5pPv2/1)



## Exercise 5
**Find the links including the parentheses for the following:** 

```
Survey and RCT Data
Slides:(https://docs.google.com/presentation/d/1WrouKjnDDaEQTiuXLtEToMqzG8Kt4D2fXNiw3OpFLCM/edit?usp=sharing)
Video: (https://kaltura.berkeley.edu/media/ECON+148%2C+LEC+001+%28Spring+2023%29/1_v7mxpk3x/288222162)
```

[Regex101 Link](https://regex101.com/r/vUm3Q4/1)


## Exercise 6
**Find the links not including the parentheses for the following:** 

```
Survey and RCT Data
Slides:(https://docs.google.com/presentation/d/1WrouKjnDDaEQTiuXLtEToMqzG8Kt4D2fXNiw3OpFLCM/edit?usp=sharing)
Video: (https://kaltura.berkeley.edu/media/ECON+148%2C+LEC+001+%28Spring+2023%29/1_v7mxpk3x/288222162)
```

[Regex101 Link](https://regex101.com/r/vUm3Q4/1)


## Exercise 7
**Find the base URL for the following (e.g. https://docs.google.com)**

```
https://docs.google.com/presentation/d/1WrouKjnDDaEQTiuXLtEToMqzG8Kt4D2fXNiw3OpFLCM

https://kaltura.berkeley.edu/media/ECON+148%2C+LEC+001+%28Spring+2023%29/1_v7mxpk3x/288222162
```

[Regex101 Link](https://regex101.com/r/FeGOpy/1)


## Reference Solution
<details class="details-example">
    <summary>Click here to display solution</summary>
    <ul>
        <li>Ex1: ex\w*</li>
        <li>Ex2: \d*</li>
        <li>Ex3: API key: (.*)\s</li>
        <li>Ex4: \s(\d{4})\s</li>
        <li>Ex5: \(.*\)</li>
        <li>Ex6: \((.*)\)</li>
        <li>Ex7: https:\/\/.+?\/</li>
    </ul>
</details>

<br>


