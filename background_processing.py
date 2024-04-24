import os
import shutil
import glob


def xml_move_for_inference(all_inference_files_path, destination_folder):   
    

    # 원본 폴더의 첫 번째 XML 파일을 대상 폴더로 이동
    if all_inference_files_path:
        # print("_--------")
        # 원본 폴더와 대상 폴더 경로 설정
        # print(all_inference_files_path)
        first_xml_file_path = all_inference_files_path
        first_xml_file_name = os.path.basename(first_xml_file_path)
        # print("fr:", first_xml_file_path)
        # print("fr_name:", first_xml_file_name)
        medi_name = first_xml_file_path.split("/")[6]
        country_name = first_xml_file_path.split("/")[7]
        
        # print(medi_name)
        # print(country_name)
        # source_path = os.path.join(first_xml_file, first_xml_file)
        destination_path = os.path.join(destination_folder, "{}_{}_".format(medi_name, country_name) + first_xml_file_name)
        # print(first_xml_file_path, destination_path)
        shutil.move(first_xml_file_path, destination_path)
        # shutil.move(first_xml_file_path, first_xml_file_med_name+first_xml_file_country+"/"+destination_path)
        # os.remove(first_xml_file)
        # print(first_xml_file_country)
        # print(first_xml_file_med_name)
        print(f"{first_xml_file_path}을 {destination_folder}로 이동했습니다.")
        
    return len(all_inference_files_path)
