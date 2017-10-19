REPO = repo
APP = work.openpaper.Paperwork
APPS = $(patsubst %.json,%,$(wildcard *.json))

all: repo bundles

# uninstall:
# 	flatpak --user uninstall $(APP)
#
# install: $(patsubst %,%.flatpak,$(APP))
# 	flatpak --user install --bundle $(patsubst %,%.flatpak,$(APP))
#
# reinstall: uninstall install

clean:
	rm -rf $(patsubst %,%.app,$(APPS)) $(patsubst %,%.flatpak,$(APPS))

dist-clean: clean
	rm -rf repo .flatpak-builder

%.app: %.json
	@echo flatpak-builder $< --\> $@ \(${EXPORT_ARGS}\)
	flatpak-builder --repo=$(REPO) -s "Build of Paperwork $(@:%.app=%) `date`" ${EXPORT_ARGS} $@ $<

repo: $(patsubst %,%.app,$(APPS))
	@echo flatpak build-update-repo $(REPO) \(${EXPORT_ARGS}\)
	flatpak build-update-repo ${EXPORT_ARGS} $(REPO)

%.flatpak: repo
	@echo flatpak build-bundle $(REPO) --\> $@ \(branch: $(@:%.flatpak=%)\)
	flatpak -v build-bundle $(REPO) $@ $(APP) $(@:%.flatpak=%)

bundles: $(patsubst %,%.flatpak,$(APPS))

.PHONY: all