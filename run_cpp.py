import os
import subprocess

def run_cpp():
    cpp_dir = "cpp_practicals"
    output_dir = "cpp_outputs"
    os.makedirs(output_dir, exist_ok=True)

    files = sorted([f for f in os.listdir(cpp_dir) if f.endswith(".cpp")])

    for filename in files:
        name = filename[:-4]
        cpp_path = os.path.join(cpp_dir, filename)
        exe_path = os.path.join(cpp_dir, name)
        output_path = os.path.join(output_dir, name + ".txt")

        print(f"Compiling {filename}...")
        compile_res = subprocess.run(["g++", cpp_path, "-o", exe_path], capture_output=True, text=True)
        if compile_res.returncode != 0:
            print(f"Compilation failed for {filename}: {compile_res.stderr}")
            continue

        print(f"Running {name}...")
        # For file handling practicals, we should run them in a clean environment or same dir
        # 14.2, 14.3, 14.4 depend on each other and the file "InfoOnCpp.txt"
        # We'll run them in the current working directory.
        run_res = subprocess.run([exe_path], capture_output=True, text=True)
        with open(output_path, "w") as f:
            f.write(run_res.stdout)
            if run_res.stderr:
                f.write("\nError Output:\n" + run_res.stderr)

        # Cleanup executable
        if os.path.exists(exe_path):
            os.remove(exe_path)

if __name__ == "__main__":
    run_cpp()
