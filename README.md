# DVS Data Converter

`dvs_data_converter.py` is a Python script designed to convert Dynamic Vision Sensor (DVS) data between different formats. It supports conversion between ROS bag files (`bag`), text files (`txt`), and comma-separated values files (`csv`).

## ⚙️ Usage
```bash
python3 dvs_data_converter.py [-h] [--output {txt,csv,bag}] [--columns {txyp,xytp,ptxy,pxyt}] [--zero] files [files ...]
```

Arguments:

*   `files`: Specifies the file or files to convert.

Optional Arguments:
*   `--output` or `-o`: Specifies the desired output format for the converted data. Available options include txt for text files, csv for comma-separated values files, and bag for ROS Bag files.
*   `--columns` or `-c`: Specifies the column order for text and CSV files. You can choose from four options: txyp, xytp, ptxy, and pxyt. The default value is txyp.
*   `--zero` or `-z`: Adds a time offset to start the data at t = 0.

## 📚 Examples
Convert ROS bag file to text file:
```bash
./dvs_data_converter.py input.bag -o txt
```

Convert ROS bag file to CSV file with specific column order:
```bash
./dvs_data_converter.py input.bag -o csv -c pxyt
```

Convert ROS bag file to CSV file and shift time:
```bash
./dvs_data_converter.py input.bag -o csv -z
```

## 📝 License

Distributed under the GPLv3 License. See [`LICENSE`](https://github.com/raultapia/dvs_data_converter/tree/main/LICENSE) for more information.

## 📬 Contact

[Raul Tapia](https://raultapia.com) - raultapia@us.es
