# Running Python remeshing project
The code was tested both on an Ubuntu and Window OS. The commands below are for Unix systems. Adjust the instructions for different operating systems.   
1. Navigate to the Project Directory: Change to the project directory where `main.py` is located:  
``` bash
cd <path_to_your_project_directory> 
```
2. Set Up Your Environment: Ensure you have the required Python environment. 
You can create it using the `environment.yml` file included in the project. Run the following command in your terminal:  
``` bash
conda env create -f environment.yml
```
3. Activate the environment:  
```bash
conda activate DGPcourse
```

4. Run the Main Script: Use the following syntax to run the remeshing script:
```bash
python3 main.py <model_name> [options]
```  
Replace <model_name> with the path to your model file (e.g., .obj, .json, or .off format). 

Data can be found in the  `samples` folder.  

**Available Options**: You can customize the execution with various options:  
* --no_sliver: Don’t run sliver triangles checks before edge flipping improves runtime by ~50% but yields worse results.  
* --foldover <FOLDOVER>: Set the foldover angle threshold (default: π/9).  
* --num_iters <NUM_ITERS>: Specify the number of iterations for remeshing (default: 5).  
* --L_factor <L_FACTOR>: Set the factor for computing target edge length (default: 0.9).  
* --save_stats: Save statistics before and after remeshing.  
* --visualize: Visualize the mesh after remeshing.  
* --save_to_obj: Save the remeshed model in .obj format.  
* --verbose_timing: Print additional timing information.  

**Help Command** : To see all available options and their descriptions, run:
```bash
python3 main.py --help
```

**Example Command**:  
Here’s an example command incorporating options:  
```bash
python3 main.py samples/iphi_bad10k.off --num_iters 10 --no_sliver --visualize --save_to_obj
```

# Running Surface Evolver
All simulations were originally run on Windows.  

First, install Surface Evolver program to your machine as instructed in the [Evolver’s page](https://kenbrakke.com/evolver/evolver.html). 
Make sure you set Evolver to open files with the `.fe` extension.

The github repo contains a simulation folder with `.fe` files, which are the simulations that were in the demo at our project presentation during the semester, and from which the images showing our remeshing quality were taken.
The naming scheme for the files is:  
```
(full/sml)_volume_(no/wt)_remeshing
```
Where:  
* `full` - Enough volume to keep all the boundary conditions.  
* `sml` - Small volume which would create a split in the mass, only connecting two of the boundary conditions.  
* `no` - No remeshing in the optimization process.  
* `wt` - With remeshing in the optimization process, the optimization process itself is unchanged.   

The simulation process itself is split into user-controlled steps, which are grouped into s1, s2 and s3 commands in the Evolver’s command language for ease of execution, with the same naming convention for the commands in all simulations.

In the `simulation` folder there is also the `timing` folder, in which are the same simulations but without visualization and without waiting for user inputs. And also a Python script to time these simulations. The data presented in the timing results is generated from the commands: 

```
python time_simulations.py "full_volume_no_remeshing.fe > NUL 2>&1" "full_volume_wt_remeshing.fe > NUL 2>&1" -r 10
```

```
python time_simulations.py "sml_volume_no_remeshing.fe > NUL 2>&1" "sml_volume_wt_remeshing.fe > NUL 2>&1" -r 10
```

