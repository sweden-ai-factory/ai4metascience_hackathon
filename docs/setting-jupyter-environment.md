# Setup Jupyter on LUMI Supercomputer 

You should now be able to log in to LUMI using the [LUMI On-Demand web interface](https://www.lumi.csc.fi/public/).

Click the **Log in to LUMI** button and select **Jupyter for Courses**.

### 1. Settings for Jupyter for Courses

Below are the recommended settings for configuring your interactive Jupyter session.

#### General settings

- **Reservation:** Select `neurips_hackathon`, the reservation assigned to the hackathon.
- **Project:** Select `project_465002387` – RISE Research Institutes of Sweden AB / ENCCS Training

- **Course module:** Select the appropriate module for the course.
  - `ai4metascience_hackathon`
- **Working directory:** Select `/scratch/project_465002387`

#### **Show custom resource settings:** Enable this option if you need to configure additional resource parameters.

Select the resources required for your course.

- **Partition:** Choose `dev-g`
- **Number of CPU cores:** Specify the number of CPU cores required. predefined value is: 8
- **Memory (GiB):** Specify the required memory. predefined is: 16 GiB
- **Number of GPUs (MI250 GCDs):** Specify the number of GPUs required. predefined is: 1
- **Time:** Specify the maximum session duration in `d-hh:mm:ss` or `hh:mm:ss` format. predefined is: 4:00:00 
- **Save settings:** choose a name for your configuration and save your settings

### 2. Launching the Jupyter Session
Click **Launch** to submit your Jupyter session. Wait a few minutes for the interactive session to start. Once the session is ready, click **Connect to Jupyter**.

You should now have access to the interactive Jupyter environment and the course materials.