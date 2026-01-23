import os
import subprocess

def run_python():
    py_dir = "python_practicals"
    output_dir = "python_outputs"
    os.makedirs(output_dir, exist_ok=True)

    files = sorted([f for f in os.listdir(py_dir) if f.endswith(".py")])

    for filename in files:
        name = filename[:-3]
        py_path = os.path.join(py_dir, filename)
        output_path = os.path.join(output_dir, name + ".txt")

        print(f"Running {filename}...")
        run_res = subprocess.run(["python3", py_path], capture_output=True, text=True)
        with open(output_path, "w") as f:
            f.write(run_res.stdout)
            if run_res.stderr:
                f.write("\nError Output:\n" + run_res.stderr)

if __name__ == "__main__":
    run_python()
