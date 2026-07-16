import customtkinter as ctk
from pydantic import BaseModel, Field, ConfigDict





class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LightSound")
        self.geometry("900x400")

        self.fixtureManager = FixtureManager(self)
        manager = self.fixtureManager.createProfileLightPanel()
        manager.grid(row=0, column=0, padx=5, pady=5)


class Fixture(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(json_schema_extra={"placeholder": "Profile name"})
    description: str = Field(json_schema_extra={"placeholder": "Brief profile description"})
    startChannel: int = Field(json_schema_extra={"placeholder": "Initial channel"})
    totalChannels: int = Field(json_schema_extra={"placeholder": "Total channels"})

    def status(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
        frameStats = ctk.CTkFrame(parent)
        for indx, (key, value) in enumerate(self.model_dump().items()):
            stat = ctk.CTkLabel(frameStats, text=f"{key}: {value}")
            stat.grid(row=indx, column=0, sticky="w", padx=4, pady=2)
        return frameStats

class FixtureManager():
    def __init__(self, frame: ctk.CTkFrame):
        self.profileFields = {}
        self.profiles = []
        self.lights = []
        #original frame app
        self.frame = frame

    def saveProfileLight(self):
        try:
            data = {k: v.get() for k, v in self.profileFields.items()}
            # testing area 

            # crear modelo(lo carga automaticamente en los campos correspondientes)
            newProfileLight = Fixture(**data)
            self.profiles.append(newProfileLight)
            lightLen = len(self.profiles)
            lightRow = (lightLen // 4)
            lightColumn = (lightLen % 4)
            lightFrame = self.createFrameLight(newProfileLight)
            lightFrame.grid(row=lightRow,column=lightColumn,sticky="ws")
        except Exception as e:
            print(f"Error al crear: {e}")
    def createProfileLightPanel(self) -> ctk.CTkFrame:
        frame = ctk.CTkFrame(self.frame)
        title = ctk.CTkLabel(frame, text="Create a light profile.")
        title.grid(row=0, column=1, padx=5, pady=5)
        description = ctk.CTkLabel(frame, text="Create a profile for a light")
        description.grid(row=1, column=1, padx=5, pady=5)
        btnSave = ctk.CTkButton(frame, text="Save profile.", command=self.saveProfileLight)
        btnSave.grid(row=4, column=1, pady=5)

        for indx, (key, place) in enumerate(Fixture.model_fields.items()):
            label = ctk.CTkLabel(frame, text=f"{key}:")
            label.grid(row=2, column=indx, padx=5, pady=5)
            entry = ctk.CTkEntry(frame, placeholder_text=place.json_schema_extra['placeholder'])
            entry.grid(row=3, column=indx)
            self.profileFields[key] = entry
        return frame
    def removeFrame(self, frame: ctk.CTkFrame):
        frame.destroy()
    def createFrameLight(self, fix: Fixture) -> ctk.CTkFrame:
        frameLight = ctk.CTkFrame(self.frame)
        sliderObj = Sliders(frameLight,fix)
        sliders = sliderObj.initChanSlidersPanel()
        sliders.pack(side="right")
        status = fix.status(frameLight)
        status.pack(side="left")
        removeBtn = ctk.CTkButton(frameLight,text="Destroy",width=140,height=28,command=lambda: self.removeFrame(frameLight))
        removeBtn.pack(side="bottom")
        return frameLight
    

class Sliders():
    def __init__(self, frame: ctk.CTkFrame, light: Fixture):
        self.frame = frame
        self.light = light
    def initChanSlidersPanel(self) -> ctk.CTkFrame:
        frame = ctk.CTkFrame(self.frame)
        start = int(self.light.startChannel)
        total = int(self.light.totalChannels)
        for i in range(start, start + total):
            lbl = ctk.CTkLabel(frame, text=str(i))
            lbl.grid(row=0, column=i, padx=2)
            slider = ctk.CTkSlider(frame, from_=0, to=255, orientation="vertical")
            slider.grid(row=1, column=i, padx=2)
            slider.set(0)
        return frame

app = App()
app.mainloop()
