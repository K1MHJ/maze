CXX := clang++
CXXFLAGS := -std=c++17
TARGET_LIB := ./bin/dllMain.so
LD := clang++
LDFLAGS := -std=c++17 -shared
SRC_DIR = src
OBJ_DIR = obj

all : $(TARGET_LIB)

clean :
	rm -rf $(OBJ_DIR) $(TARGET_LIB)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -c $< -o $@

CPP_FILES = $(wildcard $(SRC_DIR)/*.cpp)
OBJ_FILES = $(CPP_FILES:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

DEP_FILES = $(OBJ_FILES:%.o=%.d)
-include $(DEP_FILES)

$(TARGET_LIB): $(OBJ_FILES)
	@echo "Building Library $(value TARGET_LIB)"
	@echo ""
	mkdir -p $(@D)
	$(LD) $(LDFLAGS) $^ -o $@

.PHONY: all
