CC := g++
CFLAGS := -Wall -g

SRCS := $(file)
OBJS := $(patsubst %.cpp, out/%.out, $(SRCS))

all: $(OBJS)

$(OBJS): $(SRCS)
	$(CC) $(CFLAGS) -o $(OBJS) $(SRCS)

clean:
	rm -rf out/*.out
