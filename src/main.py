from rmbg import worker
import cv2 as cv
import argparse
from file_import import find_figure, det_path, get_dir_filename
import os
def main():
    parser = argparse.ArgumentParser(description='A background-removing app')
    parser.add_argument('-i', '--input', required=True, help='Input file path')
    parser.add_argument('-t', '--tolerance', type=int, default=40, help='Tolerance value (default: 40)')
    args = parser.parse_args()
    input_dir = args.input
    isdir = det_path(input_dir)
    if isdir:
        output_dir = input_dir
        figure_list = find_figure(input_dir)
        output_folder = os.path.join(output_dir, "output_figs")
        if not os.path.exists(output_folder):
            os.mkdir(output_folder)
        for figure_dir in figure_list:
            figure = worker(img_dir=figure_dir)
            new_filename = get_dir_filename(figure_dir)[1] + "_TSBG.png"
            cv.imwrite(os.path.join(output_folder,new_filename),figure)
    else:
        output_dir, pic_filename = get_dir_filename(input_dir)
        figure = worker(img_dir=input_dir)
        output_filename = pic_filename + "_TSBG.png"
        cv.imwrite(os.path.join(output_dir,output_filename),figure)

if __name__ == "__main__":
    main()
