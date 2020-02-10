# Mensural-score-to-CMN-score
This tool converts a Mensural MEI file encoding a scored-up version of a mensural piece<sup>[1](#one)</sup> into a CMN MEI file encoding this score in modern values. The Mensural MEI score used as input contains all the rhythmic information for all the voices; in other words, it encodes the exact duration of every note by using the attributes `@dur`, for note shape, and `@num` and `@numbase`, to encode the perfect / imperfect / altered quality of that particular note. The **Mensural MEI Score to CMN MEI Score Translator** divides the notes into `<measure>` elements according to the time signature provided by the user.

## Usage
To run the script, one needs four parameters. Two of them are related to the files:
- `<input_file>` is the path of the Mensural MEI file to be converted into CMN.
- `<output_file>` is the path of the resulting (CMN MEI) file.

And the other two are related to the time signature:
- `count` corresponds to the number of beats per measure.
- `unit` corresponds to the beat unit (e.g., '4' for quarter note and '2' for half note).

The parameters are expected to be entered as follows:
```
$ python mensural_to_cmn.py <input_file> <output_file> count unit
```

## Example
An example of the performance of the **Mensural MEI Score to CMN MEI Score Translator** is given by the files `Example_mensural.mei` and `Example_CMNed_6-1.mei`. The `Example_mensural.mei` file encodes an excerpt of a piece in mensural notation and score format obtained from the [Measuring Polyphony Project](https://measuringpolyphony.org). The piece from which this excerpt comes from is the motet [Se paour d'umble astinence / Diex, tan desir / \[TENOR\]](https://measuringpolyphony.org/display.html?/assets/mensural/diex_MENSURAL.mei). The following command translates the mensural score encoded in `Example_mensural.mei` into modern values using a 6/1 time signature (i.e., 6 semibreves—whole notes—per measure), and encodes the resulting CMN score into the `Example_CMNed_6-1.mei` file:
```
$ python mensural_to_cmn.py Example_mensural.mei Example_CMNed_6-1.mei 6 1
```

## Notes:
<a name="one">**1</a>:** Music in mensural notation is normally written in separate parts. MEI allows to encode this music in its original (mensural) values, but one can encode it both in a <parts> representation or a <score> representation. For the latter, it is necessary to encode the duration of the notes as well (this includes encoding the note shape as well as the perfect / imperfect / altered quality of a note). Scripts to pass from a separate-parts representation to a score representation, still preserving the original notation, have been developed (see: [Automatic Mensural Scoring-up Tool](https://github.com/ELVIS-Project/scoring-up)).